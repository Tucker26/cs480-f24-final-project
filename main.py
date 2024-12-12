from flask import Flask
from minio import Minio
import os

# This defines the main Flask object.
app = Flask(__name__)

# MinIO configuration
MINIO_URL = os.getenv('MINIO_URL', 'localhost:5000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'your-access-key')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'your-secret-key')
BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME', 'my-bucket')

# MinIO client initialization
minio_client = Minio(
    MINIO_URL,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False  # Set to True if using HTTPS
)

# Ensure the bucket exists
def ensure_bucket_exists(bucket_name):
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

ensure_bucket_exists(BUCKET_NAME)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
