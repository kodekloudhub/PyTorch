"""
Create a transform pipeline. 

The first step of the pipeline is to resize the image to 100 by 100 pixels. 

The second step of the pipeline is to randomly horizontally flip the image 50% of the time. 

The third and final step is to randomly distort the image by changing the contrast of the image with a minimum of .7 and a maximum of 1.2. 

Apply the transformation using v2 of the API.
"""
from ____.____ import ____ 
from PIL import Image

# load the image into memory
image = Image.open('images/dog/dog-5.jpg')

# Create the Pipeline transform
pipeline = ____.____([
    ____.____(____),
    ____.____(____),
    ____.____(____) 
])

# Apply the pipeline
pipeline_image = ____(____)
