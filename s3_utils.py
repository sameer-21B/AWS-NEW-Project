from datetime import datetime as d
import boto3 as b3
from io import StringIO
import pandas as pd
import numpy as np
import pickle
import json

AWS_REGION="ap-south-1"
client=b3.client("s3",region_name=AWS_REGION)
BUCKET_NAME="ecom-data-7060"
ACCOUNT_ID="379803466558"

def create_s3_buck(aws_region=AWS_REGION,bucket_name=BUCKET_NAME):
    location = {'LocationConstraint':aws_region}
    resp = client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    print("AMAZON S3 BUCKET : {} has been created".format(bucket_name))

#create_s3_buck(bucket_name="emr-hdfs-bkp")

def delete_s3_buck(aws_region=AWS_REGION,bucket_name=BUCKET_NAME,acc_id=ACCOUNT_ID):
    resp = client.delete_bucket(Bucket=bucket_name,ExpectedBucketOwner=acc_id)
    print("AMAZON S3 BUCKET : {} has been deleted".format(bucket_name))

#delete_s3_buck()

def list_all_buck():
    resp=client.list_buckets()
    for buck in resp['Buckets']:
        print(buck['Name'])

#list_all_buck()

def upload_to_s3_buck(bucket_name=BUCKET_NAME,file_nm="./ecom_data.csv",ky='ecom_data_base'):
    resp=client.upload_file(file_nm,Bucket=bucket_name,Key=ky)
    print("object: {} has been created in bucket: {}".format(ky,bucket_name))

upload_to_s3_buck("command-scripts-01","sqoop_script.sh","hadoop_mv_cmd_original.sh")

def delete_from_s3_buck(bucket_name=BUCKET_NAME,ky='ecom_data_base'):
    client.delete_object(Bucket=bucket_name,Key=ky)
    print("object: {} has been deleted from bucket: {}".format(ky,bucket_name))

#delete_from_S3_buck()