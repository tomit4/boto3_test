import boto3
import logging
import logging

import os
from dotenv import load_dotenv

load_dotenv()


def list_bucket():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            print('Buckets exist..')
            for bucket in response['Buckets']:
                print(f'  {bucket["Name"]}')
    except Exception as e:
        logging.error(e)
        return False
    return True


# NOTE: Unklikely to use, but look into creating new folder
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except Exception as e:
        logging.error(e)
        return False
    return True


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        #  response = s3_client.upload_file(file_name, bucket, object_name)
        s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True


def download_file(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket, object_name, file_name)
    except Exception as e:
        logging.error(e)
        return False
    return True


def delete_file(bucket, key_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_object(Bucket=bucket, Key=key_name)
    except Exception as e:
        logging.error(e)
        return False
    return True


def delete_bucket(bucket):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_bucket(Bucket=bucket)
    except Exception as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    list_bucket()

    # Calling create_bucket()
    #  result_create = create_bucket('phlint-app-s3-test-create', 'us-west-2')
    #  if result_create:
    #  print('bucket got created successfully!')
    #  else:
    #  print('bucket creation failed...')

    # Calling upload_file()
    #  result_upload = upload_file("./test.jpg",
    #  "phlint-app-s3-test-create",
    #  "test.jpg")
    #  if (result_upload):
    #  print("bucket file uploaded successfully!")
    #  else:
    #  print("bucket file upload failed!!")

    # Calling download_file()
    #  result_download = download_file("./downloaded_test.jpg",
    #  "phlint-app-s3-test-create", "test.jpg")
    #  if (result_download):
    #  print("bucket file downloaded successfully!")
    #  else:
    #  print("bucket file download failed!")

    # Calling delete_file()
    #  result_delete = delete_file(
    #  'phlint-app-s3-test-create',
    #  'test.jpg',
    #  )
    #  if result_delete:
    #  print('bucket file deleted successfully!')
    #  else:
    #  print('bucket file delete failed...')

    # Calling delete_bucket()
    #  result_delete_bucket = delete_bucket('phlint-app-s3-test-create')
    #  if result_delete_bucket:
    #  print('bucket deleted successfully!')
    #  else:
    #  print('bucket delete failed...')
