#!/bin/bash

printf "Installing python-venv and making python3 the default major version on this system:\n"

sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install python3-venv python-is-python3 -y

printf "Installing pip module for the current user...\n"

wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py
python ./get-pip.py

printf "Installing pipx for the current user...\n"

python3 -m pip install --user pipx
python3 -m pipx ensurepath
echo 'eval "$(register-python-argcomplete pipx)"' >> ~/.profile
source ~/.profile

printf "Installing pyinfra for the current user...\n"

python3 -m pipx install pyinfra

printf "Starting deployment..."

pyinfra inventory.py deploy.py --use-sudo-password
