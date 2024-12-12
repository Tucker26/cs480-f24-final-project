from flask import Flask, request, send_file, send_from_directory, jsonify
from minio import Minio
from minio.error import S3Error
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# This defines the main Flask object.
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)  # Set log level
handler = logging.FileHandler('app.log')  # Create file handler
app.logger.addHandler(handler)

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
        app.logger.error("Missing environment variables")
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
        app.logger.error(f"MinIO Client Error: {e}")
        return None

@app.route('/download')
def index():
    return send_from_directory('.', 'download.html')

@app.route('/download', methods=['POST'])
def download_file():
    bucket = 'my-bucket'
    filename = request.form['filename']
    app.logger.info(f"Requested file: {filename}")

    # Initialize MinIO client
    client = get_minio_client()
    if not client:
        return jsonify({"error": "Failed to connect to MinIO"}), 500

    # Download file from MinIO
    try:
        local_path = f'/tmp/{filename}'  # Ensure this directory exists
        client.fget_object(bucket, filename, local_path)
        return send_file(local_path, as_attachment=True, download_name=filename)
    except S3Error as e:
        app.logger.error(f"Error downloading file: {e}")
        return jsonify({"error": "Failed to download file"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
