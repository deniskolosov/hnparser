#!/usr/bin/env bash

cd /code || return
pip3 install --no-cache-dir -r requirements.txt

mkdir -p .tmp
mkdir staticfiles
touch db.sqlite3
python3 manage.py migrate
python manage.py collectstatic --no-input --clear
gunicorn test_appfollow.wsgi:application --bind 0.0.0.0:8000