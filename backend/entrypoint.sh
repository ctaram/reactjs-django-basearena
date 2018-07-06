#!/usr/bin/env sh
# migrate changes to database
python manage.py makemigrations && python manage.py migrate

# start the development server
python manage.py runserver 0.0.0.0:8000
