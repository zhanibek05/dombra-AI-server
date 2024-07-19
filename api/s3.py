import boto3
from .aws_settings import *

def upload_file(file_name, key):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param key: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    bucket = AWS_STORAGE_BUCKET_NAME
    # Upload the file
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME,
    )

    try:
        response = s3_client.upload_file(
            file_name,
            bucket,
            key,
            ExtraArgs={'ACL': 'public-read'},
        )
        print("Response: ", response)
    except Exception as e:
        print(e)
        return
    
    file_url = f'https://{bucket}.s3.amazonaws.com/{key}'
    return file_url