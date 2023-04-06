import json
import logging
import uuid
import boto3
from decimal import Decimal
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')
table_name = 'learning-dynamodb-dynamodb-table'

serializer = TypeSerializer()
deserializer = TypeDeserializer()

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

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

    if 'Item' not in ret:
        return {
            "statusCode": 404,
            "body": json.dumps(
                {
                    "message": "Not Found",
                }
            ),
        }

    item_python_dict = {
        k: deserializer.deserialize(v)
        for k, v in ret['Item'].items()
    }

    return {
        "statusCode": 200,
        "body": json.dumps(item_python_dict, default=decimal_default_proc),
    }

def post(event, context):

    # ボディ部をパース
    body = json.loads(event['body'], parse_float=Decimal)

    if body is None:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {
                    "message": "Bad Request",
                }
            , default=decimal_default_proc),
        }

    # GUIDを生成
    channel_id = str(uuid.uuid4())

    body['channel_id'] = channel_id

    # Bodyの値をDynamoDBの型に変換
    item_dynamodb_json = {
        k: serializer.serialize(v)
        for k, v in body.items()
    }

    options = {
        'TableName': table_name,
        'Item': item_dynamodb_json,
    }
    dynamodb.put_item(**options)

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }

def put(event, context):

    channel_id = event['pathParameters']['channel_id']

    # ボディ部をパース
    body = json.loads(event['body'], parse_float=Decimal)

    if body is None:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {
                    "message": "Bad Request",
                }
            , default=decimal_default_proc),
        }

    body['channel_id'] = channel_id

    # Bodyの値をDynamoDBの型に変換
    item_dynamodb_json = {
        k: serializer.serialize(v)
        for k, v in body.items()
    }

    options = {
        'TableName': table_name,
        'Item': item_dynamodb_json,
    }
    dynamodb.put_item(**options)

    return {
        "statusCode": 200,
        "body": json.dumps(body, default=decimal_default_proc),
    }

def delete(event, context):

    channel_id = event['pathParameters']['channel_id']

    options = {
        'TableName': table_name,
        'Key': {
            'channel_id': {'S': channel_id}
        }
    }
    dynamodb.delete_item(**options)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Deleted",
            }
        , default=decimal_default_proc),
    }
