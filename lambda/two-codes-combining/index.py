import json
import boto3
from pytz import timezone
import pytz
from help import print_name
from datetime import datetime

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    tz = timezone("Asia/Calcutta")
    print(datetime.now(tz))
    bucketlist = []
    print_name("hello from shaik")
    for bucket in s3.buckets.all():
        bucketlist.append(bucket.name)
    return {
        "statusCode": 200,
        "body": bucketlist
    }
