import boto3
from boto3.session import Session
from botocore.exceptions import ClientError
import os
import json
import logging
import time

# set up logging
logging.basicConfig(level=logging.INFO)

#create a new session
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



# define constants
DEFAULT_REGION ='us-east-1'
TEST_BUCKET_NAME = 'my-test-bucket'

# aws clients with session
s3_client = session.client('s3',region_name=us-east-1)

def  create_s3_bucket():
    try:
        s3_client.create_bucket(Bucket=TEST_BUCKET_NAME)
    except ClientError as e:
        logger.error(e)
        return False
    return True

def  delete_s3_bucket():
    try:
        s3_client.delete_bucket(Bucket=TEST_BUCKET_NAME)
    except ClientError as e:
        logger.error(e)
        return False
    return True

def  list_s3_buckets():
    try:
        response = s3_client.list_buckets()
    except ClientError as e:
        logger.error(e)
        return False
    return response['Buckets']

def  upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logger.error(e)
        return False
    return True

#main function to create bucket
if __name__ == '__main__':
    def  main():
    # create bucket
    if create_s3_bucket():
        logger.info(f'Bucket {TEST_BUCKET_NAME} created successfully')

# call main function
main()
