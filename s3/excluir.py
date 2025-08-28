import boto3

s3client = boto3.client("s3", region_name="us-east-1");

response = s3client.delete_object(Bucket="ivan-gabriel-trapp-2004-my-bucket", Key="bomba.txt")

print("Objeto excluído com sucesso!")