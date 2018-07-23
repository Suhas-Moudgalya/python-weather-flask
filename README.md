Prerequisites
==============
pip install flask.

pip install requests.

pip install --upgrade setuptools (If required).

pip install mysqlclient==1.3.9 (If required).

pip install flask_mysqldb.

pip install PyYAML.

Steps to be followed
====================
1. Signup to openweathermap and generate api-key.Use that api-key inside url in app.py file.  

2. Create a database called "flaskapp" in mysql. then Create a table called "weather" with three columns namely "city", "zipcode" and "temparature". Edit "db.yaml" file and replace db credentials in file with your local db credentials. 

3. Run "python app.py" command inside project folder.

4. Open browser and hit http://127.0.0.1:5000/



