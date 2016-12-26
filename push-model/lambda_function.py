import os
import json
import urllib
import boto3
print ('loading function')

s3 = boto3.client('s3')
def lambda_handler(event, context):
    # TODO implement
    print ("hello")
    print os.environ
    print ("Received event: " +json.dumps(event, indent=2))
    print("Printing Bucket \n")
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    print (json.dumps(bucket))
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    print ("printing key")
    print (key)
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(response['ContentLength'])
        print('printing contect type')
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this funciton.'.format(key, bucket))
        raise e
