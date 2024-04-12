#!/bin/sh
poetry run python manage.py createsuperuser --noinput;
poetry run python manage.py migrate;
poetry run python manage.py shell
poetry run python manage.py runserver 0.0.0.0:8000;