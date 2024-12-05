"""
Utilize Accuracy from torchmetrics to compute accuracy.

Be sure to set the model to evaluation model as well as set the code to not compute gradients.
"""
from load_data import test_loader
# Import modules
import ____
import torch

# Initialize the accuracy metric as a multiclass task and set number of classes to 2
accuracy_metric = ____.____(____=____, ____=____)

# Function for 
def evaluate_model(model):
    
    # Set model to evaluation mode
    ____.____
    # Disable gradient computation
    with ____.____:  
        # Loop over the test dataloader
        for i, data in enumerate(____, 0):
            inputs, labels = data
            outputs = model(inputs)

            # Get predicted class
            _, predicted = torch.max(outputs.data, 1)

            # Update the accuracy metric with predictions and true labels
            accuracy_metric.update(predicted, ____)

    # Compute the final accuracy
    final_accuracy = accuracy_metric.____
    print(f"Accuracy: {final_accuracy * 100}%")
