# Restricted Website
This is a restricted website written in Python and MySQL.

### The web site includes:
```
Welcome page
Login page
Registration page
Admin area
```

### User attributes include:
```
First name
Last name
Email
Username
Admin yes/no
```

### Standard Users are able to: 
```
1. Authenticate and see welcome page (Just login and you will be redirected to your welcome page.)
2. Edit own properties (Edit the profile after logging in.)
3. Set their password on the first login
```
First login is verified by a MySQL database and then resetting the password is automatically offered.
Anyway, a user can reset its password by adding '/change-password' to the root path.

### Admin is able to:
```
1. Do the same as standard users.
2. Edit other users properties.
3. Make other user admin.
4. Reset user passwords.
```

# Global Dependencies:
```
sudo apt-get install virtualenv
sudo apt-get install python3-pip
sudo apt-get install default-libmysqlclient-dev
sudo apt-get install mysql-server
sudo apt-get install python3-dev
sudo apt-get install python-dev
sudo apt-get install python-django-common
```

# Virtual Env:
Run:
```
virtualenv your_virtual_env_name
source your_virtual_env_name/bin/activate
pip install mysql-python
pip3 install setuptools
pip3 install wheel
pip3 install -r require3.txt
```
Following are equivalent commands for the above pip3 command.
The above pip3 command will automatically install inside your virtual environment these libraries:
```
pip3 install django
pip3 install django-crispy-forms
pip3 install Pillow
pip3 install mysqlclient
pip3 install mysql-connector
```

# Run The Django Server
```
sudo mysql -u root
>> create database mydb;
>> grant all privileges on *.* to 'khen'@'localhost' identified by 'khen';
>> exit;

sudo python3 manage.py migrate
sudo python3 manage.py runserver
```
browse to http://localhost:8000

## Create an admin
first admin through terminal:
```
sudo python3 manage.py createsuperuser
```

## Topics included:
```
Django
MVC
Relational database
MySQL
Object-relational mapping (ORM)
db migrations
Restricted pages
Secure Authentication
Virtualenv
Bootstrap
```
## Related Topics (parallel technologies):
```
Docker
Irrelational databases
phpMyAdmin
Apache server
Node.js
```
