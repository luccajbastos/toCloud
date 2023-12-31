#!/bin/sh

if [ -z "$PORT" ]; then
  PORT=8000
fi

python3 manage.py flush --no-input
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:$PORT