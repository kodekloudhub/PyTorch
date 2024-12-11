# Use official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /opt/app

# Install CPU versions of PyTorch
#RUN pip install torch==2.4.1 torchvision==0.19.1 --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./flask_app .

# Create a user and group for running the app
RUN groupadd -r pytorch && useradd --no-log-init -r -g pytorch -m pytorch

# Change ownership of the app directory
RUN chown -R pytorch:pytorch /opt/app

# Switch to the created user
USER pytorch

# Expose the port for Flask
EXPOSE 8000

# Command to run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
