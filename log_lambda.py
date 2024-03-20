import json


def lambda_handler(event, context):
    # Parse input event
    # input_data = json.loads(event["body"])
    print("EEE event", event)

    # # Process input data (example: concatenate "Hello, " with the provided name)
    # name = input_data["name"]
    greeting = f"Hello, you!"

    # Create response body
    response_body = {"message": greeting}

    # Return response
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response_body),
    }
