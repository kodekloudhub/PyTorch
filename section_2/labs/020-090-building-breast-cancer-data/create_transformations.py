"""
Define `train_transform` and `val_transform` pipelines. 

For the `train_transform` we need the following in our pipeline in the following order: 
Resize of 128 x 128 pixels
Set to Grayscale
30 degrees random rotation
50% chance of a random horizontal flip
converted to a tensor
normalized to mean and standard deviation of 0.5 for 1 channel

For the `val_transform` we need the following: 
Resize of 128 x 128 pixels
Set to Grayscale
converted to a tensor
normalized to mean andstandard deviation of 0.5 for 1 channel 

Use V2 API
"""
# Import transforms version 2
from ____ import ____

# Train Pipeline
____ = ____.____([
    ____.____((____, ____)),
    ____.____(),
    ____.____(degrees=____),
    ____.____(p=____),
    ____.____(),
    ____.____((____), (____))
])

# Validation Pipeline. Hint: Copy
____ = ____.____([
    ____.____((____, ____)),
    ____.____(),
    ____.____(),
    ____.____((____), (____))
])
