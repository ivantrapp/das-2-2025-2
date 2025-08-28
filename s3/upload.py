import boto3

s3client = boto3.client("s3", region_name="us-east-1")

s3client.upload_file("./s3/bomba.txt", "ivan-gabriel-trapp-2004-my-bucket", "bomba.txt")

print("Upload realizado com sucesso!")