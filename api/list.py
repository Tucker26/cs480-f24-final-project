from flask import jsonify
from minio import S3Error

from main import app, minio_client, BUCKET_NAME


@app.route('/list', methods=['GET'])
def list_file():
    try:
        objects = minio_client.list_objects(
            bucket_name=BUCKET_NAME
        )

        return jsonify({"message": "Files listed successfully", "files": objects}), 200

    except S3Error as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
