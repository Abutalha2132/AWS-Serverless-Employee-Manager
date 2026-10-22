
import json
import os
from decimal import Decimal
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


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o) if o % 1 == 0 else float(o)
        return super().default(o)


def respond(status, body):
    return {
        "statusCode": status,
        "headers": HEADERS,
        "body": json.dumps(body, cls=DecimalEncoder)
    }


def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    try:
        if params.get("employeeid"):
            result = table.get_item(
                Key={"employeeid": params["employeeid"]}
            )
            item = result.get("Item")

            if not item:
                return respond(404, {"message": "Employee not found"})

            return respond(200, item)

        items = []
        result = table.scan()
        items.extend(result.get("Items", []))

        while "LastEvaluatedKey" in result:
            result = table.scan(
                ExclusiveStartKey=result["LastEvaluatedKey"]
            )
            items.extend(result.get("Items", []))

        return respond(200, items)

    except ClientError as e:
        print("DynamoDB error:", str(e))
        return respond(500, {"message": "Could not read employees"})
