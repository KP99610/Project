import boto3
import json

lambda_client = boto3.client('lambda', region_name='us-east-1')

function_name = 'mys3function'

# Simulated S3 Event Payload
payload = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "myprojects3bhavana"
                },
                "object": {
                    "key": "myfile.txt"
                }
            }
        }
    ]
}

response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
)

response_payload = response['Payload'].read().decode('utf-8')
print("Lambda response:")
print(response_payload)
