# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /api_app

# Copy the requirements file into the container
COPY requirements.txt /api_app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /api_app/

# Expose port 80 for external access
EXPOSE 80

# Define environment variable
ENV NAME=ml-model-api-docker

# Set the maintainer label
LABEL maintainer="jospablo777 <jospablo777@gmail.com>" # Modify this as needed

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]