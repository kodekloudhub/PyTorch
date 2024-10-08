#!/bin/bash

# Set hostname
hostname pytorch

# data directory
mkdir -pv pytorch/data

# install Python
apt-get update && \ 
    apt-get install -y python3 python3-pip python3-venv

# Additional packages
apt-get install -y ffmpeg libsm6 libxext6

# Activate python environment
python3 -m venv venv
source venv/bin/activate

# Create the requirements file
cat << 'EOF' > requirements.txt 
datasets==3.0.1
matplotlib==3.9.2
pandas==2.2.3
pillow==10.4.0
torch==2.4.1
torchaudio==2.4.1
torchvision==0.19.1
EOF
    
pip3 install -r requirements.txt

# Install and start code server
curl -fsSL https://code-server.dev/install.sh | sh
cat /root/.config/code-server/config.yaml
code-server --bind-addr 0.0.0.0:9000
