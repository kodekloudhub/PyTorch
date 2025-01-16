#!/bin/bash

# Install metric server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# update deployment
kubectl patch -n kube-system deployment metrics-server --type=json \
  -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'

# install Python
apt-get update && \ 
    apt-get install -y python3 python3-pip python3-venv
pip3 install requests

# Download the repo
git clone https://github.com/kodekloudhub/PyTorch.git

# Install and start code server
curl -fsSL https://code-server.dev/install.sh | sh
cat /root/.config/code-server/config.yaml
code-server --bind-addr 0.0.0.0:9000
