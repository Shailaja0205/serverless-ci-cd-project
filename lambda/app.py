import json

def lambda_handler(event, context):

    response = {
        "message": "Serverless CI/CD Project Working Successfully!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }