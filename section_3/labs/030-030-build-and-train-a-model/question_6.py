"""
Create a training loop for 10 epochs. 

Be sure to initialize the loss for the current epoch as `running_loss`.

Clear the gradients, get the model predictions

Calculate the loss, compute the gradients

Update the module parameters

Accumulate the loss for the current epoch.
"""
from pre import train_dataloader
from question_2 import model
from question_4 import criterion
from question_5 import optimizer

# Set number of epochs
N_EPOCHS = ____

# Run the training loop for each epoch
for epoch in range(N_EPOCHS):
    
    # Initialize the running loss for the current epoch
    ____ = ____
    
    # Loop over the training data in batches
    for i, data in enumerate(train_dataloader, 0):
        inputs, labels = data
        # Set labels for binary float
        labels = labels.unsqueeze(1).float()
        # Clear the gradients for the optimizer
        ____.____
        # Get model predictions    
        outputs = ____(inputs)
        # Calculate the loss with the loss function
        loss = criterion(____, ____)
        # Compute the gradients of the loss
        loss.____ 
        # Update the model parameters
        optimizer.____
        # Accumulate the loss for the epoch
        ____ += loss.item()  

    # Print the epoch and running loss
    print(f"Epoch: {epoch} Loss: {____/len(train_dataloader)}")
