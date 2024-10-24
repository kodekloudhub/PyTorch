"""
Create a dataloader from our dataset named cd_dataset called cd_dataloader and then iterate through a batch and print the features and labels shape. 

When creating the dataloader, set the size of the batch to 4.  
"""
from question_3 import cd_dataset
# Import dataloader utility here
from ____.____.____ import ____

# Create the dataloader called cd_dataloader and set size to 4. 
____ = ____(dataset=cd_dataset, ____=____, shuffle=True)

# Iterate through this dataloader like we did above
features, labels, urls = next(iter(____))

# Print the batch size and the number of labels
print(f"Features batch shape: {features.____}")
print(f"Labels batch size shape: {labels.____}")
