"""
Define `train_transform` and `val_transform` pipelines. 

For the `train_transform` we need the following in our pipeline in the following order: 
Resize of 256 x 256 pixels
50% chance of a random horizontal flip
converted to a tensor
normalized to mean and standard deviation of 0.5 across the board

For the `val_transform` we need the following: 
Resize of 256 x 256 pixels
converted to a tensor
and normalized to mean
standard deviation of 0.5 across the board

Use V2 API
"""
# Import transforms version 2
from ____ import ____

# Train Pipeline
____ = ____.____([
    ____.____((____, ____)), 
    ____.____(p=____),
    ____.____, 
    ____.____(mean=[____, ____, ____], std=[____, ____, ____])
])

# Validation Pipeline. Hint: Copy
____ = ____.Compose([
    ____.____((____, ____)),
    ____.____, 
    ____.____(mean=[____, ____, ____], std=[____, ____, ____])
])
