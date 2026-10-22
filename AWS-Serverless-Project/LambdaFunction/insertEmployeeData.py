
import json
import os
import boto3
from botocore.exceptions import ClientError

TABLE_NAME = os.environ.get("TABLE_NAME", "employeeData")
ALLOWED_ORIGIN = os.environ.get(
    "ALLOWED_ORIGIN",
    "https://d1mtnyauw7ctxt.cloudfront.net"
)

table = boto3.resource("dynamodb").Table(TABLE_NAME)

HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
}


def respond(status, body):
    return {
        "statusCode": status,
        "headers": HEADERS,
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    try:
        raw_body = event.get("body")

        if isinstance(raw_body, str):
            body = json.loads(raw_body or "{}")
        elif isinstance(raw_body, dict):
            body = raw_body
        else:
            body = event

        if not isinstance(body, dict):
            return respond(400, {"message": "Request body must be a JSON object"})

    except (json.JSONDecodeError, TypeError):
        return respond(400, {"message": "Body must be valid JSON"})

    employee_id = str(body.get("employeeid", "")).strip()
    name = str(body.get("name", "")).strip()

    if not employee_id or not name:
        print("Missing required fields. Event:", json.dumps(event))
        return respond(400, {
            "message": "employeeid and name are required"
        })

    item = {
        "employeeid": employee_id,
        "name": name,
        "email": str(body.get("email", "")).strip(),
        "department": str(body.get("department", "")).strip(),
        "salary": str(body.get("salary", "")).strip(),
    }

    try:
        table.put_item(
            Item=item,
            ConditionExpression="attribute_not_exists(employeeid)",
        )
    except ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code == "ConditionalCheckFailedException":
            return respond(409, {
                "message": f"Employee {employee_id} already exists"
            })

        print("DynamoDB error:", str(e))
        return respond(500, {"message": "Could not save employee"})

    return respond(201, {
        "message": "Employee saved",
        "employee": item
    })
