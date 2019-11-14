FROM python:3.6

WORKDIR /code

ENTRYPOINT ["/code/docker-entrypoint-django.sh"]