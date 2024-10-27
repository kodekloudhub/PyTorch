""""
Apply a pipeline to a Dataset. 

The pipeline will have 2 steps. 
1. The first step is to transform an image into a tensor. 
2. The second step is to normalize an image using 0.5 for all mean and standard deviation values for RGB channels. 

Create a dataset from the MNIST preloaded dataset and apply pipeline to the dataset.

Use version 1 of the transforms API.
"""
import ____.____
from ____ import ____

# Create the pipeline transform
transform = ____.____([
    ____.____,
    ____.____(____)
])

# Create the dataset 
mnist_ds = ____.____.____(root='mnist', train=False, download=True, ____=____)
