# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest
RUN pip install --no-cache-dir pytest
RUN pip install requests
RUN pip install sealights-python-agent


# Run pytest when the container launches
CMD ["sl-python", "pytest", "--tokenfile", "sltoken.txt", "--teststage", "Automation", "--labid", "docker_go_sealights"]