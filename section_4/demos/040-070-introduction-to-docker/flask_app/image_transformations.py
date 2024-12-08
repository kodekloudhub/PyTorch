import torch
from torchvision.transforms import v2

# Define the image preprocessing transformations
preprocess = v2.Compose([
    v2.Resize((224, 224)),  # Resize image to 224x224
    v2.ToImage(), 
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
])
