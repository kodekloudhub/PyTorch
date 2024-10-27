"""
Using v2 of the transforms API, create a random horizontal flip of the image. 

The probability that the transformation takes place should be 75%.
"""
from ____.____ import ____
from PIL import Image

# Load the image to memory
image = Image.open(('images/dog/dog-2.jpg'))

# Create the transformation
transform = ____.____(____)
# Apply the transformation
rhf_image = ____(____)
