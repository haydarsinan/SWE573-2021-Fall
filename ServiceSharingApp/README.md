# SWE573-2021-Fall
These are Django Web Framework Shortcuts and Terminal Commands!!
* Django
* Create project: django-admin.py startproject ServiceSharingApp
* Runserver: python manage.py runserver
* CreateApp: python manage.py startapp ServicEventPool
* Add new app to apps in Settings
* URL Revisions from urls.py (add include to import)

```bash
python manage.py migrate
Create Tables from Models:  python manage.py makemigrations
python manage.py migrate
```

## How to run on Docker

```bash
$ docker rmi -f $(docker images -a -q)
$ docker container prune
$ docker-compose up --build
$ docker exec -it servicesharingapp_web_1 /bin/bash
```