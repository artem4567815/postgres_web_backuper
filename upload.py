import boto3

from config import *

class S3Uploader:
    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key, bucket):
        self.__session = boto3.session.Session()
        self.__bucket = bucket
        self.__aws_access_key = aws_access_key_id
        self.__s3 = self.__session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net',
            region_name=str(region_name),
            aws_access_key_id=str(self.__aws_access_key),
            aws_secret_access_key=str(aws_secret_access_key),
        )

    def upload(self, file_name):
        self.__s3.upload_file(file_name, self.__bucket, 'dir/subdir/' + file_name)

    def get_list_object_in_bucket(self):
        for key in self.__s3.list_objects(Bucket=self.__bucket)['Contents']:
            print(key['Key'])


if __name__ == "__main__":
    upload = S3Uploader(S3_REGION, S3_access_key_id, S3_secret_access_key, S3_bucket)
    upload.upload('text.txt')
    upload.get_list_object_in_bucket()