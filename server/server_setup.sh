#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

# Install a fancier shell with more features than bash
apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install some OS dependencies that are useful for working with the vm:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv
# Install the server proxy 
sudo apt-get install -y -q nginx
# for gzip support in uwsgi which allows for working with compressed files
sudo apt-get install --no-install-recommends -y -q libpcre3-dev libz-dev

# Stop the hackers by adding a little security and block hackers.
sudo apt install fail2ban -y

# Expose the ports we need using ufw (Uncomplicate FireWall).
ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

# Log in and logout now and check that everything is working.

# Basic git setup
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=720000'

# Be sure to put your info here:
git config --global user.email "aambrioso1@gmail.com"
git config --global user.name "aambrioso"

# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/alex_site
mkdir /apps/logs/alex_site/app_log
cd /apps

# Create a virtual env for the app.
cd /apps
python3 -m venv venv
source /apps/venv/bin/activate # To activate: $ /apps . venv/bin/activate

# Can check $ which python here

# 
pip install --upgrade pip setuptools # update pip
pip install --upgrade httpie glances # allows for testing web apps, lets us look at system
pip install --upgrade uwsgi # takes a while 


# We will edit .zshrc so that the virtual environment is activated as soon as we log into the vm
# $ nano .zshrc
# add:  
# source /apps/venv/bin/activate
# at the bottom of the script.  
# Log in and log out to check.

# clone the repo:
cd /apps
git clone https://github.com/aambrioso1/pypi-flask-app

# Setup the web app:
cd cd /apps/alex_site/
pip install -r requirements.txt

# We can check the if the app runs and start another shell and run app:
# http localhost:5000 (use the appropriate local port)

# Need have wgsi.py in app folder.  We can run ExecStart command to check if it works outside of daemon.
# Use another terminal http localhost:5000 to check.

# Copy and enable the daemon
cp /apps/alex_site_new/server/alex_site_new.service /etc/systemd/system/alex_site_new.service

systemctl start alex_site_new
systemctl status alex_site_new
systemctl enable alex_site_new

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

# Check nginx.py to see that server_name is correct.

cp /apps/alex_site_new/server/alex_site_new.nginx /etc/nginx/sites-enabled/alex_site_new.nginx
update-rc.d nginx enable # 
service nginx restart


# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
# Should choose redirect to https
add-apt-repository ppa:certbot/certbot
apt install python-certbot-nginx
certbot --nginx -d fakepypi.talkpython.com
