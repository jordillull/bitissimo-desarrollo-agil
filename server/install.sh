#!/bin/sh
# Simple install script for serving a static website with nginx

# update the repository
sudo apt-get update

# install nginx package
sudo apt-get install -y nginx

# remove default config file
sudo rm /etc/nginx/sites-enabled/default

# set ourt custom config file pointing the document root to
# the vagrant shared directory /site
sudo tee /etc/nginx/sites-available/site.conf <<EOF
server {
    listen 80;

    root /site;

    location / {
      index  index.html index.htm;
    }
}
EOF

# enable the configuration just created
sudo ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/site.conf

# make sure nginx will be started on system startup
sudo update-rc.d nginx enable

# restart nginx to apply the changes
sudo service nginx restart
