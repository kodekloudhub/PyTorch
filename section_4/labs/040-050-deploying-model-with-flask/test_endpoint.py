"""
Test the model deployment by sending a sample image to the endpoint.
"""
import base64
import requests
import os

# set current directory
work_dir = os.path.dirname(os.path.abspath(__file__))

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Open the image and transform to b64 encoded string
with open(os.path.join(work_dir, 'sample-input.jpg'), 'rb') as img_file:
    base64_string = base64.b64encode(img_file.read()).decode('utf-8')

# Create the payload for the request
payload = {
    "image": base64_string
}

# Send POST request
response = requests.____(____, 
                         json=payload, 
                         headers=headers)

# Print the response
print("Response JSON:", response.json())
