import json

def lambda_handler(event, context):

    response = {
        "message": "GitHub Actions CI/CD Working Successfully!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }