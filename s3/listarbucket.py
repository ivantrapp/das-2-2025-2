import boto3

s3client = boto3.resource("s3", region_name="us-east-1")

bucket = s3client.Bucket("ivan-gabriel-trapp-2004-my-bucket")

for obj in bucket.objects.all():
    print(obj.key + str(obj.size))