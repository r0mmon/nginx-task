#!/usr/bin/env bash
ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo service nginx restart
cd /home/box/web/ && gunicorn -b 0.0.0.0:8080 -w 4 hello:wsgi_application&
cd /home/box/web/ && gunicorn -b 0.0.0.0:8000 -w 4 ask/wsgi:application&
