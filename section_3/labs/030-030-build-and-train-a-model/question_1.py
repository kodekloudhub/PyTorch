"""
Create a Class to build a Neural Network in a PyTorch manner. 

Begin by importing the Neural Network module from PyTorch and name your Class “Neural Network”. 

Then define your layers as follows: 1) A 2D convolutional layer, 2) a 2D max pooling layer and 3) a fully connected layer. 

Once layers have been defined, then define the flow through the layers as follows: 1) pass through conv layer with ReLU activation, then apply max pooling, 2) flatten the output from the convolutional layers, and then 3) pass through fully connected layer with sigmoid.

"""
import torch
# Import the nn module
import ____.____ as nn 
import torch.nn.functional as F

# Create a Neural Network that inherits the Neural Network module
class ____(____.____):
    # Function for defining layers
    def __init__(self):
        # Initialize superclass for automatic parameters
        super(____, self).__init__()
        # Define a 2D convolutional layer
        self.conv1 = ____.____(in_channels=3, out_channels=16, kernel_size=3)
        # Define a 2D max pooling layer
        self.pool = ____.____(kernel_size=2, stride=2)
        # Define a fully connected layer
        self.fc1 = ____.____(16 * 16 * 16, 1)

    # Function for defining flow through the network. 
    def forward(self, x):
        # Pass through conv layer with ReLU activation, then apply max pooling
        x = self.____(F.____(self.____(x)))
        # Flatten the output from the convolutional layers
        x = x.view(-1, 16 * 16 * 16)
        # Apply Sigmoid for probalities from the fully connected layer
        x = torch.sigmoid(self.____(x))
        # Pass through fully connected layer with ReLU activation
        x = F.____(self.____(x))
        
        return x
    
