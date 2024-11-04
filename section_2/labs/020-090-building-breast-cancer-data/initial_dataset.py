"""
Create a custom PyTorch Dataset called initial_dataset that contains the initial data from our annotations file full_image_data.csv. 

Once again we will use Pandas to read in our annotations file. 

We will then return each index with image_path and label.
"""
import pandas as pd
# Import Dataset from torch data utils
from ____ import ____


class BreastCancerDataset(Dataset):
    def __init__(self, annotations_file):
        self.image_labels = pd.read_csv(annotations_file)

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, idx):
        image_path = self.image_labels.iloc[idx, 0]
        label = self.image_labels.iloc[idx, 1]
        # Return image path and label
        return ____, ____

# Create the initial dataset
____ = ____(annotations_file=____)
