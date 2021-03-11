#!/bin/bash

# basic server - displays hostname

# install python 3
yum update -y
yum install python3 -y

# install git
yum install git -y

# clone to ~/app
git clone https://github.com/rhgksrua/hostname-server.git app

cd /app

# venv
python3 -m venv venv
.venv/bin/activate

#install Flask
pip install Flask

export FLASK_APP=app.py
flask run --host=0.0.0.0