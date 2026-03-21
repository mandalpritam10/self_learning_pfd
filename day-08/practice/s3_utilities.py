"""

inside view of making a client and get the bucket details

"""


# import boto3

# s3_client=boto3.client("s3") #creating a client for s3 access

# buckets_data=s3_client.list_buckets()

# print(type(buckets_data),"\n")

# for key in buckets_data.keys():
#     print(key)

# print("\n")
# print(type(buckets_data["ResponseMetadata"]))
# print(type(buckets_data["Buckets"]))
# print(type(buckets_data["Owner"]))

# print("\n")
# for key,value in buckets_data["ResponseMetadata"].items():
#     print(f"{key} : {value}")

# print("\n")
# for bucket in buckets_data["Buckets"]:
#     print(bucket)

# print("\n")
# for key,value in buckets_data["Owner"].items():
#     print(f"{key} : {value}")

# print("\n")
# for bucket in buckets_data["Buckets"]:
#     print(bucket["Name"])




"""

s3,ec2 and play with the services

"""

import boto3
# import boto3.session (when we use sessions)

class AWSutils:
    def __init__(self):
        self.s3=self.get_connection("s3")
        self.ec2=self.get_connection("ec2")

    def get_connection(self,service):

        """
        this is using session, we will work on it later, 
        now no need, as aws configure is enough for now
        """
        # session=boto3.Session(
        #     access_id="xyz",
        #     secret_key="xyz",
        #     region_name="xyz"
        # )
        # client_details=session.client(service)
        # return client_details

        client_details=boto3.client(service)
        return client_details

    def show_buckets(self):
        buckets_data=self.s3.list_buckets()
        for bucket in buckets_data["Buckets"]:
            print(bucket["Name"])
    
    def create_buckets(self,bucket_name):
        try:
            response = self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': 'us-east-2',
                },
            )
            if response["ResponseMetadata"]["HTTPStatusCode"]==200:
                print("Bucket created successfully")
            else:
                print("Error occured while creating the bucket")
        except Exception as e:
            print(e)

    def upload_to_bucket(self,file_path,bucket_name,key_name):
        self.s3.upload_file(file_path,bucket_name,key_name)
        print("fill uploaded successfully")

    def show_regions(self):
        response=self.ec2.describe_regions()
        for region in response["Regions"]:
            print("Regions are: ",region["RegionName"])

    def show_available_regions(self):
        response=self.ec2.describe_availability_zones()
        for available_zone in response["AvailabilityZones"]:
            print("Available zones are: ",available_zone["RegionName"])


print("Start","\n")

if __name__ == "__main__":
    print("Hello from aws class wali file")
    a1=AWSutils()
    a1.show_buckets()
    print("\n")

    a1.create_buckets("someone-ki-bucket-2")
    print("\n")

    a1.upload_to_bucket("output.json","mandalpritam10-first-bucket","output.json")
    print("\n")

    a1.show_regions()
    print("\n")

    a1.show_available_regions()
    print("\n")

print("Exit")