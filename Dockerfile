# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /api_app

# Copy the requirements file into the container at /app
COPY requirements.txt /api_app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /api_app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=ml-model-api-docker

# Set the maintainer label
LABEL maintainer="jospablo777 <jospablo777@gmail.com>"

# Run main.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]