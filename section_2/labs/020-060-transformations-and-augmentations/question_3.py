"""
Using v1 of the transforms API, resize the following image to 250 pixels by 300 pixels. 

Use the pillow library to first load the image.
"""
from torchvision import ____
from ____ import ____

# Load the image into memory
image = ____.____(('images/dog/dog-1.jpg'))

# Create the resize transform
resize_transform = ____.____(____)

# Apply the transform
resized_image = ____(____)
