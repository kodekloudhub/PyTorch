# Use official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /opt/app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./flask_app .

# Expose the port for Flask
EXPOSE 8000

# Create a user to run the app
USER pytorch 

# Command to run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
