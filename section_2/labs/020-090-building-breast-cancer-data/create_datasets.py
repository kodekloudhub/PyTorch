"""
Using the custom PyTorch Dataset Class provided, create a training dataset called train_dataset and a validation dataset called val_dataset. 

For each use the proper transformations and the proper annotations file. 

Also be sure to create the label encoding for our 2 labels (benign and malignant) and pass the label_encoder as the target_transform.
"""
from create_transformations import train_transform, val_transform
import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class CustomImageBreastCancerDataSet(Dataset):
    def __init__(self, annotations_file, image_dir, transform, target_transform):
        self.image_labels = pd.read_csv(annotations_file)
        self.image_dir = image_dir
        self.transform = transform
        self.target_transform = lambda y: target_transform[y]

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.image_labels.iloc[idx, 0])
        image = Image.open(image_path)
        label = self.image_labels.iloc[idx, 1]
        image = self.transform(image)
        label = self.target_transform(label)
        
        return image, label


# Label encoding
label_encoding = {____: ____, ____: ____}

# Create the Training Dataset
____ = ____(
    annotations_file=____, 
    image_dir='data', 
    transform=t____, 
    target_transform=____
)

# Create the Validation Dataset
____ = ____(
    annotations_file=____, 
    image_dir='data', 
    transform=____, 
    target_transform=____
)
