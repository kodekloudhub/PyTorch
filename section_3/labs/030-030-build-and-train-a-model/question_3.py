"""
Print the model weights and bias that is easy to read
"""
from question_2 import model

# Loop through the parameters in human readable
for name, param in ____:
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")
