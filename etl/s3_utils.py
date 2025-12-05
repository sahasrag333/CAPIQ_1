import boto3
import json
from io import BytesIO

s3 = boto3.client("s3")

def read_json_from_s3(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(obj["Body"].read())
