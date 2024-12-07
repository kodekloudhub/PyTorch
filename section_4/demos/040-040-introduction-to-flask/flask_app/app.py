from flask import Flask, request, jsonify
from torchvision import models
from image_transformations import preprocess
from PIL import Image
import torch
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Load any other environment variables or variables here

# Load the MobileNetV3 Large pre-trained model
model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)
model.eval()  # Set model to evaluation mode


# Health endpoint
@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to confirm the app is running.
    """
    return jsonify({'status': 'healthy'}), 200

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Error handling
    try:
        # Extract Base64 string from request JSON
        data = request.json
        if 'image' not in data:
            # Return and error if there is no image in the request
            return jsonify({'error': 'No image provided'}), 400
        
        # Decode the Base64 image string
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Preprocess the image
        transformed_img = preprocess(image).unsqueeze(0)
        
        # Perform inference
        with torch.no_grad():
            output = model(transformed_img)
            _, predicted = torch.max(output.data, 1)
        
        # Return our prediction
        return jsonify({'prediction': predicted.item()})
    
    # Fail with our error in the response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
