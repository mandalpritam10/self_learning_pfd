import boto3
import json 

class AWSutils:

    def __init__(self):
        self.s3=self.get_connection("s3")
        self.ec2=self.get_connection("ec2")

    def get_connection(self,service):
        client_details=boto3.client(service)
        return client_details

    def show_buckets(self):
        response=self.s3.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]

    def create_buckets(self,bucket_name):
        try:
            response=self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint' : 'us-east-2'
                }
            )

            if response["ResponseMetadata"]["HTTPStatuscode"] == 200:
                return "Bucket Created Successfully"
            else:
                return "Failed to create this bucket"
        except Exception as e:
            return str(e)
        
    def upload_to_bucket(self,file_path,bucket_name,key_name):
        self.s3.upload_file(file_path,bucket_name,key_name)
        return "File uploaded Successfully"

    def show_regions(self):
        response=self.ec2.describe_regions()
        return [region["RegionName"] for region in response["Regions"]]

    def show_available_zones(self):
        response=self.ec2.describe_availability_zones()
        return [available_zone["RegionName"] for available_zone in response["AvailabilityZones"]]

def main():
    a1 = AWSutils()
    data = {}

    data["buckets"] = a1.show_buckets()
    data["bucket_creation"] = a1.create_buckets("someone-ki-bucket-2")
    data['upload status'] = a1.upload_to_bucket("output.json","mandalpritam10-first-bucket","output.json")
    data["regions"] = a1.show_regions()
    data["available_zones"] = a1.show_available_zones()

    return data

if __name__ == "__main__":

    response=main()

    for key,value in response.items():
        print(f"{key} : {value}","\n")
        
    with open("aws_report.json","w+") as json_file:
        json.dump(response,json_file,indent=4)

    print("Data saved to json file successfully")