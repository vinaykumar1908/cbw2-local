#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd cbw2; python manage.py createsuperuser --no-input)
fi
(cd cbw; sudo gunicorn cbw.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
sudo nginx -g "daemon off;"
