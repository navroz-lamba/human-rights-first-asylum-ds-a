import secrets
from secrets import access_key, secret_access_key

import boto3
import os

S3 = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
                        
# uploads pdf files added to dir
for file in os.listdir():
    if '.pdf' in file:
        upload_file_bucket = "human-rights-first-asylum-analysis-documents"
        upload_file_key = 'pdf/' + str(file)
        S3.upload_file(file, upload_file_bucket, upload_file_key)