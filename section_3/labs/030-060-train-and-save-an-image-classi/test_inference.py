"""
Test inference 
"""
from pre import val_transform, work_dir
from load_model import model
from PIL import Image
import torch
import os

# Load and preprocess a sample image
image_path = os.path.join(work_dir, 'sample-input.jpg')
image = Image.open(image_path)

# Apply the transformation
transformed_image = val_transform(image)

# Set eval mode
model.____
# Perform inference
output = ____(transformed_image)
# Print the prediction
print(f"Prediction: {output}")
