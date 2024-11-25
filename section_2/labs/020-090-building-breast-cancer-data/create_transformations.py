"""
Define `train_transform` and `val_transform` pipelines. 

For the `train_transform` we need the following in our pipeline in the following order: 
Resize of 128 x 128 pixels
Set to Grayscale
30 degrees random rotation
50% chance of a random horizontal flip
converted to a tensor
normalized mean (0.485, 0.456, 0.406) and standard deviation (0.229, 0.224, 0.225) for 3 channels

For the `val_transform` we need the following: 
Resize of 128 x 128 pixels
Set to Grayscale
converted to a tensor
normalized mean (0.485, 0.456, 0.406) and standard deviation (0.229, 0.224, 0.225) for 3 channels

Use V2 API
"""
import torch
# Import transforms version 2
from ____ import ____

# Train Pipeline
____ = ____.____([
    ____.____((____, ____)),
    ____.____(degrees=____),
    ____.____(p=____),
    ____.____(), 
    ____.____(torch.float32, ____),
    ____.____(mean=[____, ____, ____], 
              std=[____, ____, ____])
])

# Validation Pipeline. Hint: Copy
____ = ____.____([
    ____.____((____, ____)),
    ____.____(), 
    ____.____(torch.float32, ____),
    ____.____(mean=[____, ____, ____], 
              std=[____, ____, ____])
])
