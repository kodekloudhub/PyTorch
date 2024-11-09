"""
Additional code that needs to run to make other code work
"""
import torch
from torch.utils.data import Dataset, DataLoader

# Random dataset
class RandomDataset(Dataset):
    def __init__(self, num_samples=100, input_size=(3, 34, 34), num_classes=2):
        self.num_samples = num_samples
        self.input_size = input_size
        self.num_classes = num_classes

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        image = torch.rand(self.input_size)
        label = torch.randint(0, self.num_classes, (1,)).item()
        return image, label

# dataset and dataloader
train_dataset = RandomDataset(num_samples=100, input_size=(3, 34, 34), num_classes=2)
train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True)
