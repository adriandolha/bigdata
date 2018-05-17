import boto3
import boto.s3.connection

access_key = 'put your access key here!'
secret_key = 'put your secret key here!'

conn = boto3.client(service_name='s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    endpoint_url='http://localhost:4572',
                    use_ssl=False
                    )
# print(conn.create_bucket(
#     ACL='public-read-write',
#     Bucket='bdsample'
# ))


for bucket in conn.list_buckets():
    print(bucket)

for item in conn.list_objects(Bucket='bdsample'):
    print(item)
