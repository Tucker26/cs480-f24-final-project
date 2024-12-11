from flask import Flask

# This defines the main Flask object.
app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file(client, bucket, object_name, file_path):
    try:
        client.fput_object(bucket, object_name, file_path)
    except:
        print("----ERROR: Upload failed----")
        return "Error Upload Failed", 500

    return "File uploaded", 200


if __name__ == '__main__':
    app.run()
