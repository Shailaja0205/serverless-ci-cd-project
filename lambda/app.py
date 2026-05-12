import json

def lambda_handler(event, context):

    response = {
        "message": "github action success test"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }