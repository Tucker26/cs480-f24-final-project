from flask import Flask
from minio import Minio

# This defines the main Flask object.
app = Flask(__name__)


@app.route('/download', methods=['GET'])
def download_file(client, bucket, object_name, file_path):
    try:
        client.fget_object(bucket, object_name, file_path)
    except:
        print("----ERROR: Download failed----")
        return "Error Download Failed", 500

    return "File downloaded", 200


if __name__ == '__main__':
    app.run()
