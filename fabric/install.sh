#!/bin/sh
# Simple install script for serving a static website with nginx

# update the repository
sudo apt-get update

# install nginx and git packages
sudo apt-get install -y nginx git-core

# remove default config file
sudo rm /etc/nginx/sites-enabled/default

# set ourt custom config file pointing the document root to
# the vagrant shared directory /site
sudo tee /etc/nginx/sites-enabled/site.conf <<EOF
server {
    listen 80;

    root /opt/site/current;

    location / {
      index  index.html;
    }
}
EOF

# prepare the repo
sudo mkdir /opt/site
sudo mkdir /opt/site/releases
sudo chown vagrant:vagrant -R /opt/site

# clone the repository
sudo -u vagrant git clone https://github.com/hugochinchilla/dumb-test.git /opt/site/git

# restart nginx to apply the changes
sudo service nginx restart
