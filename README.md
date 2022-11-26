# Django User Management

This is a template project for user management on Django. It contains two apps: one for main project logic and 
another for users. In this project User management is based on email authorization (including for superusers).
Also, two base pages inside: index.html with content both for authenticated users and not authenticated, and
secret.html, which is only for logged-in users.

> **Warning**: no css inside :)

### How to use?

#### Migrations
```bash 
python manage.py makemigrations
python manage.py migrate
```

#### Start local server
```bash 
python manage.py runserver
```

#### Create superuser
```bash 
python manage.py createsuperuser
```
