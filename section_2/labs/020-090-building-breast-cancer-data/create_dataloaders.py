"""
Create PyTorch DataLoaders for the train_dataset and the  val_dataset. 

This will define how the data is passed to the model during training and is the last step before you train the model. 

The train_loader should take in the train_dataset with a batch size of 64 and should shuffle. 

The val_loader should take the val_dataset with a batch size of 32 and should not shuffle. 
"""
from create_datasets import train_dataset, val_dataset
# Import DataLoader
from ____ import ____

# Create the training DataLoader
____ = ____(____, ____=____, shuffle=____)

# Create the Validation DataLoader
____ = ____(____, batch_size=____, ____=____)
