"""
Initialize the model and load the latest trained model from its checkpoint.
"""
from breast_cancer_net import BreastCancerClassification
# Import modules
import torch

# Initialize Model
model = ____
# load the latest checkpoint
checkpoint = ____.____("____", weights_only='true')
# Load the parameters to our model
____.____(checkpoint['____'])
# Print the model
print(model)
