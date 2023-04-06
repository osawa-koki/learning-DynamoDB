import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def ping(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "pong",
            }
        ),
    }
