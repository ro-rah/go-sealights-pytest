# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest
RUN pip install --no-cache-dir pytest

# Run pytest when the container launches
CMD ["pytest"]
