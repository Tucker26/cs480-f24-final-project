from flask import request, jsonify
from minio import S3Error

from main import app, minio_client, BUCKET_NAME


@app.route('/download', methods=['GET'])
def download_file():
    if 'filename' not in request.files:
        return jsonify({"error": "No file name in the request"}), 400

    filename = request.files['filename']
    response = None

    try:
        # Save the file to MinIO
        response = minio_client.get_object(
            bucket_name=BUCKET_NAME,
            object_name=filename
        )

        return jsonify({"message": "File downloaded successfully", "file": response}), 200

    except S3Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if response:
            response.close()
        response.release_conn()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
