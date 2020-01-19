#!/bin/sh
python test_task/manage.py migrate

gunicorn test_task.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 2 \
    --timeout 90