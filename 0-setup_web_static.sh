#!/usr/bin/env bash
# This configures our servers and set it up
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir /data
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "Hello Madness" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i '/# pass PHP scripts to FastCGI server/i \\tlocation \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\tautoindex off;\n\t\}\n' /etc/nginx/sites-available/default
sudo service nginx restart
