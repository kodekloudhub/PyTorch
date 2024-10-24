import torchvision
import pandas as pd
from PIL import Image
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

# """
# Below is showing how to create a dataset using Imagefolder
# """
print("########## Imagefolder example")
# Load all of the images with default dataset
dataset = torchvision.datasets.ImageFolder(
        root="images", # images directory
        transform=transforms.Compose([transforms.ToTensor()]))

# Print attributes of our dataset
print(f"Classes: {dataset.classes}")
print(f"Mapped Classes: {dataset.class_to_idx}")

# Create a dataloader
train_dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Iterate over the dataloader and print features and labels
# for batch_idx, (features, labels) in enumerate(train_dataloader):
train_features, train_labels = next(iter(train_dataloader))
print(f"Features batch shape: {train_features.shape}")  # Tensor shape (batch_size, channels, height, width)
print(f"Labels batch size: {train_labels.size()}")  # Labels for the batch
label = train_labels[0]
print(f"Label: {label}")


"""
Below is showing how to create a custom dataset 
"""
print("########## Custom dataset example")
# List of classes
class_list = ["cat", "dog"]

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, class_list):
        self.df = pd.read_csv(annotations_file)
        self.class_list = class_list

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, index):
        image = Image.open(self.df.file_path[index])
        img_url = self.df.file_path[index]
        # Images must be tensors
        convert_tensor = transforms.ToTensor()
        image = convert_tensor(image)
        label = self.class_list.index(self.df.label[index])

        return image, label, img_url
    
# Create the dataset
dataset = CustomImageDataset(annotations_file='section_2/demos/015-datasets-and-dataloaders/labels.csv', 
                             class_list=class_list)

# Print attributes of our dataset
print(f"Annotations data: \n{dataset.df}") 
print(f"Classes: {dataset.class_list}")

# Create a dataloader
train_dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Display image and label randomly
train_features, train_labels, train_urls = next(iter(train_dataloader))
print(f"Features batch shape: {train_features.size()}")
print(f"Labels batch size: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
img_url = train_urls[0]
# plt.imshow(img, cmap="gray")
# plt.show()
print(f"Label: {label}")
print(f"Image: {img_url}")

# Map the label to a string class
class_labels_map = {0: 'cat', 1: 'dog'}
class_label_string = class_labels_map.get(label.item())
print(f"Mapped Classes: {class_label_string}")
