"""
Create StepLR scheduler that reduces the learning rate by 0.1 every 2 epochs
"""
from modify_resnet_output import model
# Import module
import torch.nn as nn
import ____.____ as optim

# Create Loss function
criterion = nn.CrossEntropyLoss()
# Create Optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
# Create Scheduler
scheduler = optim.____.____(____, ____=____, ____=____)
