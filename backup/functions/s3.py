from datetime import datetime


class S3:

    def __init__(self, account_id, client, resource):
        self.client = client
        self.resource = resource
        self.account_id = account_id

    def upload_to_S3(self, path, bucket_name, key, content_type):

        now = datetime.now()
        folder_name = now.strftime("%m/%d/%Y")

        try:
            self.resource.meta.client.upload_file(
                path, bucket_name, Key=(folder_name + '/' + key), ExtraArgs={'ContentType': content_type})
            print("Successfully upload the file")
        except NameError:
            print("Error uploading")
