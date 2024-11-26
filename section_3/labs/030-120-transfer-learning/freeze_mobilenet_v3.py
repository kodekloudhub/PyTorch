"""
Set the last layer in the classifier layer to use 2 classes.

Freeze all layers.

Unfreeze only the final layer.
"""
from load_mobilenet_v3 import model
# import module
import ____.____ as nn

# Modify last layer of the model for 2 classes
model.classifier[-1] = ____.____(1280, ____)

# Freeze all layers
for param in ____.____:
    param.____ = ____

# Unfreeze last layer 
for param in ____.classifier[-1].____:
    param.____ = ____
