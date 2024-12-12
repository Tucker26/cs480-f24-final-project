from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# This defines the main Flask object.
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG) # Set log level
handler = logging.FileHandler('app.log') # Create file handler
app.logger.addHandler(handler)
app.logger.info(os.environ)

# Initialize MinIO client
def get_minio_client():
    s3_endpoint = os.getenv('S3_ENDPOINT')
    access_key = os.getenv('ACCESS_KEY')
    secret_key = os.getenv('SECRET_KEY')

    # Print the environment variables to debug
    app.logger.info(f"S3_ENDPOINT: {s3_endpoint}")
    app.logger.info(f"ACCESS_KEY: {access_key}")
    app.logger.info(f"SECRET_KEY: {secret_key}")

    if not s3_endpoint or not access_key or not secret_key:
        print("Missing environment variables")
        return None

    try:
        client = Minio(
            endpoint=s3_endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=False
        )
        return client
    except S3Error as e:
        print(f"MinIO Client Error: {e}")
        return None

@app.route('/list', methods=['GET'])
def list_files():
    bucket = 'my-bucket'
    if not bucket:
        return jsonify({"error": "Bucket name is required"}), 400

    # Initialize MinIO client
    client = get_minio_client()
    if not client:
        return jsonify({"error": "Failed to connect to MinIO"}), 500

    # Ensure the bucket exists
    try:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
    except S3Error as e:
        print(f"Error checking/creating bucket: {e}")
        return jsonify({"error": "Failed to ensure bucket exists"}), 500

    # List files in the bucket
    try:
        filelist = client.list_objects(bucket)
        files = [file.object_name for file in filelist]
        return jsonify({"files": files}), 200
    except S3Error as e:
        print(f"Error listing files: {e}")
        return jsonify({"error": "Failed to list files"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
