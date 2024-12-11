def list_files(client, bucket):
    try:
        filelist = client.list_objects(bucket)
        for file in filelist:
            print(file.object_name)
    except:
        print("----ERROR: File list failed----")