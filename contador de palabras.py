# programa que lee el numero de palabras de un archvo subido a s3 y te envia mensaje diciendote el nombre 
# del archivo y cuantas palabras tiene, hecho en lambda aws

import json
import boto3
import os

def lambda_handler(event,context):
    
    #todo implement
    s3 = boto3.client('s3')

    #1 get bucket name
    bucketName = event['Records'][0]['s3']['bucket']['name']
    
    #2  get the file/key name
    key = event['Records'][0]['s3']['object']['key']

    #3 fetch the file from s3
    file_content = s3.get_object(Bucket=bucketName,Key=key)["Body"].read()

    wordCount=len(file_content.split())

    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='arn:aws:sns:us-west-2:010360140913:Word_Count',
        Subject='Word Count Result',
        Message=f'The word count in the file {key} is {wordCount}'
    )