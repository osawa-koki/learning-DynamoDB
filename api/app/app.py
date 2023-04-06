import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')
table_name = 'learning-dynamodb-dynamodb-table'

def ping(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "pong",
            }
        ),
    }

def get(event, context):

    channel_id = event['pathParameters']['channel_id']

    options = {
        'TableName': table_name,
        'Key': {
            'channel_id': {
                'S': channel_id,
            }
        }
    }
    ret = dynamodb.get_item(**options)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": ret["Item"],
            }
        ),
    }
