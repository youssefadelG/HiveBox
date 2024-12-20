# Dockerfile

# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
#RUN pip install --no-cache-dir -r ./requirements.txt

# Run the Python script when the container starts
CMD ["python3", "main.py"]
