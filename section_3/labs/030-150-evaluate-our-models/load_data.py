"""
Create the test dataloader to use a batch size of 64 and ensure that it doesn’t shuffle. 
"""
# Import all necessary modules
import pandas as pd
import torch
import os
from torch.utils.data import Dataset
from PIL import Image
from torchvision.transforms import v2
from torch.utils.data import DataLoader


# Dataset Class
class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform, target_transform):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = lambda y: target_transform[y]

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = Image.open(img_path)
        label = self.img_labels.iloc[idx, 1]
        image = self.transform(image)
        label = self.target_transform(label)
        
        return image, label


# Label encoder
label_encoding = {"malignant": 0, "benign": 1}

# Transformations
test_transform = v2.Compose([
    v2.Resize((224, 224)),
    v2.ToImage(), 
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], 
                 std=[0.229, 0.224, 0.225])
])

# Current working directory
work_dir = os.path.dirname(os.path.abspath(__file__))

# Test_dataset
test_dataset = CustomImageDataset(
    annotations_file=os.path.join(work_dir, 'test_data.csv'), 
    img_dir="./", 
    transform=test_transform, 
    target_transform=label_encoding
)

# Create a Dataloader with batch size set to 64 and shuffle set to False
test_loader = ____(____, ____=____, ____=____)
