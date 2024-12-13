"""
Using pre-trained models from torchvision, load resnet18 with default Resnet18 weghts.

Set output layer to 2 classes.

Load our fine tuned model from a checkpoint.

Load the model parameters from the checkpoint. 
"""
# Import modules
import torch
import torch.nn as nn
from torchvision import ____

# Load the model from torchvision models using default weights
model = ____.____(weights=models.____.____)

# Set classes in output layer to 2
model.fc = nn.Linear(512, ____)

# Load checkpoint
checkpoint = torch.____('resnet_checkpoint.tar', weights_only=True)

# Load the model parameters from the checkpoint
model.____(____['model_state_dict']) 
# Print the model
print(model)
