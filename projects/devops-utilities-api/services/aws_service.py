
import boto3
from datetime import datetime,timezone,timedelta

def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets_details = s3_client.list_buckets()["Buckets"]
    
    current_date = datetime.now(timezone.utc).astimezone()
    old_buckets = []
    new_buckets = []

    for bucket in buckets_details:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return{
        "total_buckets":len(buckets_details),
        "total_old_buckets":len(old_buckets),
        "total_new_buckets":len(new_buckets),
        "old_buckets":old_buckets,
        "new_buckets":new_buckets
    }