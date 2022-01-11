# SWE573-2021-Fall

Deployment Link:
https://servicevent.online/

## How to build and run the application on Docker
```bash
$ docker-compose up -d --build
$ docker exec -it servicesharingapp-web-1 /bin/bash
$ python manage.py migrate
```

Alternative Way:
## How to run on Docker, Last Line is CLI in Docker

```bash
$ docker rmi -f $(docker images -a -q)
$ docker container prune
$ docker-compose up --build
$ docker exec -it servicesharingapp_web_1 /bin/bash
$ python manage.py migrate
```