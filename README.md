# Restricted Website
This is a restricted website written in Python and MySQL.

### The web site includes:
```
1. Welcome page
2. Login page
3. Registration page
4. Admin area (to access, add ‘/admin’ to the default route, e.g. ‘localhost/admin’.)
```

### User attribute includes:
```
1. First name
2. Last name
3. Email
4. Username
5. Admin yes/no
```

### Standard Users is be able to: 
```
1. Authenticate and see welcome page (Just login and you will be redirected to your welcome page.)
2. Edit own properties (By the profile page after logging in.)
3. Set their password on the first login (First login is verified by a MySQL database.)
```

### Admin is able to:
```
1. Do the same as standard users.
2. Edit other users properties.
3. Make other user admin.
4. Reset user passwords.
Clauses 2-4 are performed in the admin area.
```

# Running the server using the virtualenv:
```
1. a mysql database called 'mydb' is required:
   sudo apt-get install mysql-server
   sudo mysql -u root
>> create database mydb;

2. run the virtualenv:
   source bin/activate

3. sudo python3 manage.py runserver
```
browse to http://localhost:8000

# Creating an admin:
at django project directory:
sudo python3 manage.py createsuperuser
(for entering the /admin area of the site we have to create a superuser)

## Building from scratch:
sudo apt-get install mysql-server
sudo mysql -u root
>> create database mydb;

pip install django
pip install mysqlclient
pip install mysql-python
pip install django-crispy-forms
pip install Pillow

## Topics included:
Django
MVC
Relational database, MySQL database
MySQL shell server
db migrations
Object-relational mapping (ORM)
Restricted pages
Secure Authentication
Virtualenv

## Related Topics (parallel technologies):
Docker
Irrelational databases
phpMyAdmin
Apache server
