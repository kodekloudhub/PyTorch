"""
Normalize the image and then randomly resize it. 

The mean values for the RGB channels should all be 0.5 and the standard deviation should also be set to 0.5. 

The minimum size of the image should be 50 pixels and the maximum size of the image should be 300 pixels. 

Use v2 of the API.
"""
from torchvision.transforms import v2
from PIL import Image

# Load the image to memory
img = Image.open('images/dog/dog-1.jpg')

# Normalize() does not support PIL images.
tensor_transform = ____.____
tensor_img = tensor_transform(____)

# Normalize the image
normalize_transform = ____.____(____) 
normalize_img = ____(____)

# Randomly resize the image
rand_resize_transform = ____.____(____)
rand_resize_img = ____(____)
