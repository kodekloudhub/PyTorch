#!/bin/bash

# Set hostname
hostname pytorch

# data directory
mkdir -pv PyTorch/data

# install Python
apt-get update && \ 
    apt-get install -y python3 python3-pip python3-venv

# Additional packages
apt-get install -y ffmpeg libsm6 libxext6

# Activate python environment
python3 -m venv venv
source venv/bin/activate
    
pip3 install -r PyTorch/requirements.txt

# Install and start code server
curl -fsSL https://code-server.dev/install.sh | sh
cat /root/.config/code-server/config.yaml
code-server --bind-addr 0.0.0.0:9000
