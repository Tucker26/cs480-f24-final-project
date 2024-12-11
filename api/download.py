def download_file(client, bucket, object_name, file_path):
    try:
        client.fget_object(bucket, object_name, file_path)
    except:
        print("----ERROR: Download failed----")