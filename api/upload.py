def upload_file(client, bucket, object_name, file_path):
    try:
        client.fput_object(bucket, object_name, file_path)
    except:
        print("----ERROR: Upload failed----")