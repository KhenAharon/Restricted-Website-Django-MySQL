# Restricted Website
This is a restricted website written in Python and MySQL.

### The web site includes:
```
Welcome page
Login page
Registration page
Admin area (to access, add ‘/admin’ to the default route, e.g. ‘localhost/admin’.)
```

### User attribute includes:
```
First name
Last name
Email
Username
Admin yes/no
```

### Standard Users is be able to: 
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
Clauses 2-4 are performed in the admin area.

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
pip3 install -r require3.txt
```
It will automatically install inside your virtual environment these libraries:
```
pip install setuptools
pip3 install setuptools
pip install mysqlclient
pip install mysql-python
pip install django
pip3 install django-crispy-forms
pip install Pillow
```

# Run The Django Server
```
sudo mysql -u root
>> create database mydb;

sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo python3 manage.py runserver
```
browse to http://localhost:8000

## Create an admin:
```
sudo python3 manage.py createsuperuser
```

## Topics included:
```
Django
MVC
Relational database
MySQL database
MySQL shell server
Object-relational mapping (ORM)
db migrations
Restricted pages
Secure Authentication
Virtualenv
```
## Related Topics (parallel technologies):
```
Docker
Irrelational databases
phpMyAdmin
Apache server
```
