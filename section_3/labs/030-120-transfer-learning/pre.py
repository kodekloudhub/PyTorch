"""
This file is used to create Datasets, DataLoaders and Transformations we already created in the Build Breast Cancer data Lab
"""
import pandas as pd
import os
import torch
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
        # Transform the image
        image = self.transform(image)
        # Get the label
        label = self.target_transform(label)
        
        return image, label
    

# Label Encoding
label_encoding = {"malignant": 0, "benign": 1}

# Training Transformations
train_transform = v2.Compose([
    v2.Resize(224),
    v2.RandomRotation(degrees=30),
    v2.RandomHorizontalFlip(p=.5),
    v2.ToImage(), 
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], 
                 std=[0.229, 0.224, 0.225])
])

# set current directory
work_dir = os.path.dirname(os.path.abspath(__file__))

# Training dataset
train_dataset = CustomImageDataset(
    annotations_file=os.path.join(work_dir, 'training_data.csv'), 
    img_dir="./", 
    transform=train_transform, 
    target_transform=label_encoding
)

# Train DataLoader
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Validation Transformations
val_transform = v2.Compose([
    v2.Resize(224),
    v2.ToImage(), 
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], 
                 std=[0.229, 0.224, 0.225])
])

# Validation Dataset
val_dataset = CustomImageDataset(
    annotations_file=os.path.join(work_dir, 'val_data.csv'), 
    img_dir="./", 
    transform=val_transform, 
    target_transform=label_encoding
)

# Validation DataLoader
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)




