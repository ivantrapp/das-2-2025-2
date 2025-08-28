import boto3

s3client = boto3.client("s3", region_name="us-east-1")

s3client.create_bucket(Bucket='ivan-gabriel-trapp-2004-my-bucket', )

print("Bucket criado com sucesso!")