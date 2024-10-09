"""
Using the image module from Pillow, open the image into memory. 

Using the transforms module from torchvision, create a transformation that converts the image into a PyTorch tensor. 

Finally create a tensor from the transformation and print the size and device attributes. 
"""
from PIL import ____
from torchvision import ____

# Load the image into memory
img = ____.____("/root/PyTorch/images/pytorch-logo.png")

# Create a transformation
transform = ____.____

# Transform our image into a tensor and print it
tensor = ____(____)

print(tensor.shape, tensor.____)
