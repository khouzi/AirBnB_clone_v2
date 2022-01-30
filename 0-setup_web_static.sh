#!/usr/bin/env bash
#set up the web server

sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
printf %s "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
location /redirect_me {
 return 301 https://www.youtube.com/watch?v=k85mRPqvMbE&ab_channel=CrazyFrog;
    }
    root /var/www/html;
    error_page 404 /error404.html;
    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;
    server_name 34.139.171.141;
    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
        add_header X-Served-By 2596-web-01;
    }
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}" > /etc/nginx/sites-available/default

service nginx restart