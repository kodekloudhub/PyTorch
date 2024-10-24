from PIL import Image
import os
from torchvision import transforms

# Define the transformation to resize images to a fixed size (e.g., 224x224)
resize_transform = transforms.Resize((224, 224))

# Directory containing original images
input_dir = "images/"

# Directory to save resized images
output_dir = "resize_images/"
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# Loop through the images in the input directory
for img_file in os.listdir(input_dir):
    if img_file.endswith(('.jpg', '.png', '.jpeg')):  # Add more formats if needed
        # Load the image
        img_path = os.path.join(input_dir, img_file)
        img = Image.open(img_path)
        
        # Apply the resizing transformation
        resized_img = resize_transform(img)
        
        # Save the resized image to the output directory
        resized_img_path = os.path.join(output_dir, img_file)
        resized_img.save(resized_img_path)
        print(f"Saved resized image: {resized_img_path}")
