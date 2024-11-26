"""
Modify the last layer to output 2 classes
"""
from load_resnet_model import model
# Import module
import ____.____ as nn

# Set classes in output layer to 2
model.fc = ____.____(512, ____)

