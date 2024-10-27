"""
With v2, first transform the image into a tensor. Second, randomly crop the image at 50 x 200 pixels. 
"""
from ____.____ import v2
from PIL import Image

# Load image into memory
image = Image.open('images/cat/cat-3.jpg')

# Transform the image to a tensor and apply it
tensor_transform = v2.____
tensor_image = ____(____)

# Transform the tensor image by random crop and apply it
random_crop_transform = v2.____(____)
random_crop_image = ____(____)
