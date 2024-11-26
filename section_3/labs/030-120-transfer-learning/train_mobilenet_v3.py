"""
Train the mobilenetv3 model for 3 epochs.

Set the scheduler as well as the save it in the checkpoint every epoch.
"""
from pre import train_loader, val_loader
from freeze_mobilenet_v3 import model
from mobilenet_v3_scheduler import criterion, optimizer, scheduler
# Import modules
import torch


# Set number of epochs
N_EPOCHS = ____

for epoch in range(N_EPOCHS):
  
    ####### TRAINING
    training_loss = 0.0 
    # Set the model to training mode
    model.train()
  
    for i, data in enumerate(train_loader, 0):
       inputs, labels = data
      
       optimizer.zero_grad()  # Clear the gradients


       outputs = model(inputs)
       loss = criterion(outputs, labels)  # Calculate the loss
       loss.backward() 
       optimizer.step()  # Update model parameters
      
       training_loss += loss.item()


    ######## VALIDATION
    val_loss = 0.0
    # Set the model to evaluation
    model.eval()


    for i, data in enumerate(val_loader, 0):
       inputs, labels = data 
      
       outputs = model(inputs) 
       loss = criterion(outputs, labels) # Calculate the loss
      
       val_loss += loss.item()

    # Step the scheduler at the end of the epoch
    ____.____
   
    ######## SAVE A CHECKPOINT for each epoch
    torch.save({'epoch': epoch,
                'model_state_dict': model.state_dict(), # Save model
                'optimizer_state_dict': optimizer.state_dict(), # Save Optimizer
                'scheduler_state_dict': ____.____,  # Save Scheduler
                'train_loss': training_loss, # Save training loss
                'val_lass': val_loss}, # Save validation loss
                f'mobilenet_v3_{epoch}_checkpoint.tar')
    
    # Print the training loss and the val loss
    print(f"Epoch: {epoch} Train Loss: {training_loss/len(train_loader)} Val Loss: {val_loss/len(val_loader)}")
