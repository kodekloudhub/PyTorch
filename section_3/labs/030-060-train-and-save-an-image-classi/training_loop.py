"""
Set number of training epochs to 5 

In the training portion of the code complete the following: 
set the model to training mode
clear the gradients
calculate the loss
update the parameters with the optimizer

In the validation portion of the code:
set the model to evaluation
calculate the loss

In the checkpoint saving portion include: the model
optimizer
training loss
validation loss
save as a tar

"""
from pre import train_loader, val_loader
from create_model import model 
from loss_function_optimizer import optimizer, criterion
# Import modules
import torch 

# Set number of epochs
____ = ____

for epoch in range(N_EPOCHS): 
    
    ####### TRAINING
    training_loss = 0.0  
    # Set the model to training mode
    model.____
    
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data 
        
        ____.____  # Clear the gradients

        outputs = model(inputs) 
        loss = ____(____, labels)  # Calculate the loss 
        loss.backward()  
        ____.____  # Update model parameters 
        
        training_loss += loss.item() 

    ######## VALIDATION
    val_loss = 0.0
    # Set the model to evaluation 
    model.____

    for i, data in enumerate(val_loader, 0):
        inputs, labels = data  
        
        outputs = model(inputs)  
        loss = criterion(____, labels) # Calculate the loss
        
        val_loss += loss.item() 

    ######## SAVE A CHECKPOINT for each epoch
    torch.save({'epoch': epoch,
                'model_state_dict': ____.____, # Save model 
                'optimizer_state_dict': ____.____, # Save Optimizer
                'train_loss': ____, # Save training loss
                'val_lass': ____}, # Save validation loss
                f'{epoch}_checkpoint.____')
    
    # Print the training loss and the val loss
    print(f"Epoch: {epoch} Train Loss: {training_loss/len(train_loader)} Val Loss: {val_loss/len(val_loader)}")
