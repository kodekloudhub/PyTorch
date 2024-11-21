"""
Importing the necessary modules to create a network as well as the module for performing operations on layers 

Name the net `BreastCancerClassification` and ensure that it inherits 

Create the layers in the following order: 
2 convolutional
1 2D max pooling
3 linear layers

Use ReLU activations for connecting layers 

"""
# Import the needed modules
import ____.____ as nn
import ____.____.____ as F 

# Name the class
class ____(nn.Module):
    def __init__(self):
        super(____, self).__init__()
        # Create the layers 
        self.conv1 = nn.____(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.____(32, 64, kernel_size=3, padding=1)
        self.pool = nn.____(2, 2) 
        
        self.fc1 = nn.____(64 * 32 * 32, 256)
        self.fc2 = nn.____(256, 128)
        self.fc3 = nn.____(128, 2)

    def forward(self, x):
        # Create the layer connections 
        x = self.pool(F.____(self.conv1(x)))
        x = self.pool(F.____(self.conv2(x)))
        x = x.view(-1, 64 * 32 * 32)
        x = F.____(self.fc1(x))
        x = F.____(self.fc2(x))
        x = self.fc3(x)
        return x
