from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import requests

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        zipcode = request.form['zip']
        countrycode = request.form['cc']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+','+countrycode+'&appid=4c0d9402daa2da0af1af90a091e2d35a')
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        city = json_object['name']
        temp_f = (temp_k - 273.15) * 1.8 + 32
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO weather(city, zipcode, temparature) VALUES(%s, %s,%s)",(city,zipcode,temp_f))
        mysql.connection.commit()
        cur.close()
        return redirect('/weather')
    return render_template('index.html')

@app.route('/weather')
def weather():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM weather")
    if resultValue > 0:
        weatherDetails = cur.fetchall()
        return render_template('weather.html',weatherDetails=weatherDetails)

if __name__ == '__main__':
    app.run(debug=True)
