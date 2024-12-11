from flask import Flask
from minio import Minio

# This defines the main Flask object.
app = Flask(__name__)


@app.route('/list', methods=['GET'])
def list_files(client, bucket):
    try:
        filelist = client.list_objects(bucket)
        for file in filelist:
            print(file.object_name)
    except:
        print("----ERROR: File list failed----")
        return "Error List Failed", 500

    return "Files listed", 200


if __name__ == '__main__':
    app.run()
