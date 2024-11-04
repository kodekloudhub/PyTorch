"""
Create 3 CSV files (`training_data.csv`, `validation_data.csv`, and `testing_data.csv`) using Pandas. 

Use the indices from the split data to map the `image_path` and `label` from the `initial_dataset` and use these as columns.
"""
from initial_dataset import initial_dataset
from split_data import train_dataset, val_dataset, test_dataset
import pandas as pd

############ Training
data = []
# For each index in the training dataset indices
for idx in ____.____:
    # Extract the file_path and the label from the initial dataset 
    image_path = initial_dataset.image_labels['file_path'].loc[idx]
    label = initial_dataset.image_labels['label'].loc[idx]
    # Append path and label 
    data.append({"file_path": image_path, "label": label})

# Create a Dataframe and save as csv file
df = pd.DataFrame(data)
df.to_csv(____, index=False)

############ Validation
data = []
# For each index in the validation dataset indices
for idx in ____.____:
    # Extract the file_path and the label from the initial dataset 
    image_path = initial_dataset.image_labels['file_path'].loc[idx]
    label = initial_dataset.image_labels['label'].loc[idx]
    # Append path and label 
    data.append({"file_path": image_path, "label": label})

# Create a Dataframe and save as csv file
df = pd.DataFrame(data)
df.to_csv(____, index=False)

############# Testing
data = []
# For each index in the Testing dataset indices
for idx in ____.____:
    # Extract the file_path and the label from the initial dataset 
    image_path = initial_dataset.image_labels['file_path'].loc[idx]
    label = initial_dataset.image_labels['label'].loc[idx]
    # Append path and label 
    data.append({"file_path": image_path, "label": label})

# Create a Dataframe and save as csv file
df = pd.DataFrame(data)
df.to_csv(____, index=False)
