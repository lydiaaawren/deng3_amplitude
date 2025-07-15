# Load libraries
import boto3
import os
from dotenv import load_dotenv

# loading .env
load_dotenv()

# .env variables
aws_access_key=os.getenv('AWS_ACCESS_KEY')
aws_secret_key=os.getenv('AWS_SECRET_KEY')
aws_bucket_name=str(os.getenv('AWS_BUCKET_NAME'))

# Create S3 Client using AWS Credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Set file start and end points
local_file_location = "test_file.json"
aws_file_destination = "python-import/test_file.json"

# Upload file to s3 bucket
s3_client.upload_file(local_file_location, aws_bucket_name, aws_file_destination)

print("File uploaded")
