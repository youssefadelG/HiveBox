# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app

# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY app.py /app

# Create a non-root user and switch to it
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Run the Python script when the container starts
CMD ["python3", "/app/app.py"]