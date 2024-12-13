"""
From torchvision models, load the pre-trained mobilenet_v3_large model with default MobileNet_V3_Large_Weights weights.

Modify the last layer for 2 classes.

Load the model from checkpoint.

Load the model parameters from the checkpoint.
"""
# Import modules
import torch
import torch.nn as nn
from torchvision import ____

# Load the mobilenet_v3_large model with default weights
model = ____.____(weights=models.____.____)

# Modify last layer of the model for 2 classes as output
model.classifier[-1] = nn.Linear(1280, ____)

# Load the model from checkpoint
checkpoint = torch.____('mobilenet_checkpoint.tar', weights_only=True)

# Load the parameters from the checkpoint
model.____(____['model_state_dict']) 
# Print the model
print(model)
