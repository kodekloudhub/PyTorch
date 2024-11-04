"""
Split the initial_dataset into training, validation and testing datasets using the function from PyTorch used to randomly split data. 

Call the training data train_dataset, validation data val_dataset and the testing data test_data. 

Use 70% for training, 20% for validation and 10% for testing.
"""
from initial_dataset import initial_dataset
# Import the random split function 
from ____ import ____

# Define size of Training data
train_size = int(____ * len(initial_dataset))
# Define size of Validation data 
val_size = int(____ * len(initial_dataset))
# Finally define the rest as test 
test_size = len(initial_dataset) - train_size - val_size

# Randomly Split the data for train dataset, validation dataset and then test dataset
____, ____, ____ = ____(initial_dataset, [train_size, val_size, test_size])
