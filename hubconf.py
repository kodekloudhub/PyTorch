# Define dependencies
dependencies = ['torch']
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.hub import load_state_dict_from_url

# Dictionary point to the URL of the models
models_url = {
    'fake_model': 'https://github.com/kodekloudhub/PyTorch/raw/refs/heads/main/section_3/demos/030-105-additional-training-methods/model_state_dict.pt'
}


# Model Class
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


# Entrypoint to our fake_model
def fake_model(pretrained = False, **kwargs): 
    """
        FakeNet model
        pretrained (bool): kwargs, load pretrained weights into the model
    """
    model = FakeNet(**kwargs)

    # If pretrained is true then load the parameters from the url
    if pretrained:
        model.load_state_dict(torch.hub.load_state_dict_from_url(models_url['fake_model'], progress=True))

    return model
