import json

def lambda_handler(event, context):

    response = {
        "message": "Automatic CI/CD Deployment Successful!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }