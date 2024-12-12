# Stage 1: Base image
FROM python:3.12 AS base

# Set working directory to the /api folder
WORKDIR /cs480-f24-final-project/api

# Copy requirements.txt into the container
COPY requirements.txt /cs480-f24-final-project/requirements.txt
RUN pip install --no-cache-dir -r /cs480-f24-final-project/requirements.txt

# Copy everything from your project into the /api folder
COPY . /cs480-f24-final-project/api/

# Stage 2: Download Service
FROM base AS download
CMD ["python", "download.py"]
EXPOSE 5000

# Stage 3: List Service
FROM base AS list
CMD ["python", "list.py"]
EXPOSE 5000

# Stage 4: Upload Service
FROM base AS upload
CMD ["python", "cs480-f24-final-project/api/upload.py"]
EXPOSE 5000

