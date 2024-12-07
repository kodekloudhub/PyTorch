from flask import Flask, request, jsonify
from torchvision import models
from image_transformations import preprocess
from PIL import Image
import torch
import io
import base64
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the MobileNetV3 Large pre-trained model
try:
    logger.info("Loading MobileNetV3 Large pre-trained model...")
    model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)
    model.eval()  # Set model to evaluation mode
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise RuntimeError("Failed to load the model.") from e

# Health endpoint
@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to confirm the app is running.
    """
    response = {'status': 'healthy'}
    logger.info(f"Response for /health: {response}")
    return jsonify(response), 200

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract Base64 string from request JSON
        data = request.json
        if 'image' not in data:
            logger.warning("No image provided in the request.")
            response = {'error': 'No image provided'}
            logger.info(f"Response for /predict: {response}")
            
            return jsonify(response), 400
        
        # Decode the Base64 image string
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Preprocess the image
        transformed_img = preprocess(image).unsqueeze(0)
        
        # Perform inference
        with torch.no_grad():
            logger.info("Performing inference...")
            output = model(transformed_img)
            _, predicted = torch.max(output.data, 1)
            logger.info(f"Inference complete. Predicted class: {predicted.item()}")
        
        # Return our prediction
        response = {'prediction': predicted.item()}
        logger.info(f"Response for /predict: {response}")
        
        return jsonify(response)
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        response = {'error': str(e)}
        logger.info(f"Response for /predict: {response}")
        
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
