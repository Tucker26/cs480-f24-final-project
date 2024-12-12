from flask import request, jsonify
from minio import S3Error

from main import app, minio_client, BUCKET_NAME


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        # Save the file to MinIO
        minio_client.put_object(
            BUCKET_NAME,
            file.filename,
            file.stream,
            length=-1,  # Automatically determine size
            part_size=10 * 1024 * 1024,  # 10MB part size for multipart uploads
            content_type=file.content_type
        )

        return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200

    except S3Error as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
