# This Dockerfile shows you how you might create a container for Python-based microservices.

# YOU CANNOT USE THIS FILE AS-IS. YOU NEED TO MAKE CHANGES TO MAKE IT MATCH YOUR PROJECT.

# Use the official Python image from the Docker Hub 
FROM python:3.12 AS base

# Copy requirements.txt into the application directory
COPY requirements.txt /cs480-f24-final-project/requirements.txt

# Set the working directory to /app
WORKDIR /cs480-f24-final-project

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /c2480-f24-final-project

# **  Assume your first microservice is login.py  **

WORKDIR /cs480-f24-final-project/api

FROM base AS download

CMD ["python", "download.py"]

# Flask listens on port 5000.
EXPOSE 5000

# **  Assume your second microservice is user.py  **

FROM base AS list

CMD ["python", "list.py"]

EXPOSE 5000

FROM base AS upload

CMD ["python", "upload.py"]

EXPOSE 5000

# **  Repeat the above for as many microservices as you have.  **
