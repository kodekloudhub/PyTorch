"""
This code is a pre-requisite for questions 3-5.

Create a custom dataset class called CatDogDataset.

Fix the methods in the code needed for the Dataset class for our custom dataset.

Finally create a new dataset called cd_dataset. The annotations file is already set as well as the class list.
"""
import os
import pandas as pd
from PIL import Image
from torchvision import transforms
# Import dataset here
from ____.____.____ import ____


# Define our custom Dataset Class
class ____(____):
    # Set the methods for Dataset Class
    def ____(self, annotations_file, class_list):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        annotations_file_path = os.path.join(script_dir, annotations_file)
        self.df = pd.read_csv(annotations_file_path)
        self.class_list = class_list

    def ____(self):
        return self.df.shape[0]

    def ____(self, index):
        image = Image.open(self.df.file_path[index])
        img_url = self.df.file_path[index]
        # Images must be tensors. Ignore transformations for now.
        convert_tensor = transforms.ToTensor()
        image = convert_tensor(image)
        label = self.class_list.index(self.df.label[index])

        return image, label, img_url


# Create a custom dataset called cd_dataset
____ = ____(annotations_file='labels.csv', class_list=['cat', 'dog'])



