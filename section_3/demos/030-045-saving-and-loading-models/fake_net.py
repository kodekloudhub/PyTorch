import torch.nn as nn
import torch.nn.functional as F

class FakeNet(nn.Module):
    def __init__(self):
        super(FakeNet, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.batch_norm = nn.BatchNorm1d(50) 
        self.fc2 = nn.Linear(50, 1)        

    def forward(self, x):
        x = F.relu(self.fc1(x))              
        x = self.batch_norm(x)               
        x = self.fc2(x)                      
        return x
