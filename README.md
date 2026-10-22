# AWS Serverless Employee Manager

A serverless employee management web application built using Amazon Web Services (AWS). The application allows users to insert and retrieve employee records through a web interface connected to a REST API.

## Project Overview

This project demonstrates a serverless architecture using AWS managed services. The frontend is hosted in a private Amazon S3 bucket and delivered through Amazon CloudFront using Origin Access Control (OAC). Amazon API Gateway connects the frontend to Python-based AWS Lambda functions, while Amazon DynamoDB stores employee records.

The project provides practical experience with serverless application development, API integration, IAM permissions, CORS configuration, secure content delivery, and AWS troubleshooting.

## AWS Architecture

<img width="1536" height="1024" alt="Serverless Employee Manager AWS Architecture (1)" src="https://github.com/user-attachments/assets/8785d88e-bf03-4ce4-bbf1-5c6f3b2f0577" />


### Architecture Flow

1. A user accesses the web application through Amazon CloudFront over HTTPS.
2. CloudFront retrieves frontend files from the private Amazon S3 bucket using Origin Access Control (OAC).
3. The frontend sends GET and POST requests to Amazon API Gateway.
4. API Gateway routes requests to the appropriate Lambda function.
5. GetFunction retrieves employee records from DynamoDB.
6. InsertFunction validates and inserts employee records into DynamoDB.
7. The API response is returned to the frontend and displayed to the user.

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Stores frontend HTML, CSS, and JavaScript files in a private bucket |
| Amazon CloudFront | Delivers frontend content over HTTPS |
| Origin Access Control (OAC) | Allows CloudFront to access the private S3 origin |
| Amazon API Gateway | Exposes REST API endpoints |
| AWS Lambda | Executes Python backend functions |
| Amazon DynamoDB | Stores employee records |
| AWS IAM | Controls permissions for AWS resources |
| Amazon CloudWatch | Provides Lambda logs and monitoring |

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python
- Cloud Platform: Amazon Web Services
- API: Amazon API Gateway REST API
- Database: Amazon DynamoDB
- Content Delivery: Amazon CloudFront
- Object Storage: Amazon S3

## Application Features

- Add employee records through a web form.
- Retrieve and display employee records.
- Store employee information in Amazon DynamoDB.
- Use separate Lambda functions for insertion and retrieval.
- Integrate the frontend with backend services through API Gateway.
- Configure CORS for frontend-to-API communication.
- Deliver frontend content through CloudFront without making the S3 bucket publicly accessible.

## Project Structure

```text
AWS-Serverless-Employee-Manager/
│
├── frontend/
│   ├── index.html
│
├── lambda/
│   ├── get_function.py
│   └── insert_function.py
 architecture.png
 README.md
```

Adjust the filenames and folders to match the actual files uploaded to GitHub.

## DynamoDB Configuration

**Table name:** `employeeData`

**Partition key:** `employeeid`

**Data type:** String

The table stores the following employee attributes:

- `employeeid`
- `name`
- `email`
- `department`
- `salary`

The `employeeid` attribute identifies each employee record.

## Lambda Functions

### 1. GetFunction

Handles GET requests to retrieve employee records from DynamoDB.

Responsibilities:

- Retrieve employee records from the DynamoDB table.
- Return data in JSON format.
- Support retrieving all records or a specific record if implemented with an `employeeid` query parameter.
- Return appropriate HTTP responses and CORS headers.

### 2. InsertFunction

Handles POST requests to add employee records to DynamoDB.

Responsibilities:

- Parse the JSON request body.
- Validate required employee fields.
- Insert employee records into DynamoDB.
- Prevent duplicate employee IDs when conditional writes are configured.
- Return appropriate HTTP responses and CORS headers.

## API Gateway Configuration

The application uses an API Gateway REST API with the `/employees` resource.

| HTTP Method | Purpose |
|---|---|
| GET | Retrieve employee records |
| POST | Insert an employee record |
| OPTIONS | Handle browser CORS preflight requests |

**Deployed API endpoint:**

```text
https://vdojpubvf2.execute-api.ap-southeast-2.amazonaws.com/ApiDeploy/employees
```

The endpoint is specific to this deployment. A new deployment may use a different API ID, region, or stage.

## Secure Frontend Delivery

The frontend uses Amazon S3 and CloudFront with a private origin configuration.

- The S3 bucket remains private.
- S3 Block Public Access should remain enabled.
- CloudFront uses Origin Access Control (OAC) to retrieve files from S3.
- The S3 bucket policy grants the required access to the CloudFront distribution.
- Users access the application through the CloudFront distribution URL over HTTPS.

This configuration avoids exposing the S3 bucket directly to public users.

## Deployment Steps

### Step 1: Create the DynamoDB Table

1. Open the Amazon DynamoDB console.
2. Create a table named `employeeData`.
3. Configure `employeeid` as the partition key with the String data type.
4. Create the table.

### Step 2: Create the Lambda Functions

1. Create `GetFunction` using Python.
2. Add the employee retrieval code.
3. Create `InsertFunction` using Python.
4. Add the employee insertion code.
5. Configure the required IAM execution permissions for DynamoDB and CloudWatch Logs.

### Step 3: Configure API Gateway

1. Create or configure an API Gateway REST API.
2. Create the `/employees` resource.
3. Configure GET to invoke `GetFunction`.
4. Configure POST to invoke `InsertFunction`.
5. Configure OPTIONS and the required CORS response headers.
6. Deploy the API to the `ApiDeploy` stage.

### Step 4: Configure the Private S3 Bucket

1. Create an S3 bucket for the frontend files.
2. Upload the HTML, CSS, and JavaScript files.
3. Keep S3 Block Public Access enabled.
4. Do not enable public bucket access or rely on the S3 website endpoint.
5. Configure CloudFront Origin Access Control to access the S3 bucket.

### Step 5: Configure CloudFront

1. Create a CloudFront distribution using the S3 bucket as the origin.
2. Configure Origin Access Control (OAC).
3. Update the S3 bucket policy to allow the distribution to access the required objects.
4. Configure `index.html` as the default root object.
5. Wait for the distribution to deploy.
6. Access the application using the CloudFront distribution domain.

### Step 6: Connect the Frontend to API Gateway

Configure the API endpoint in the frontend JavaScript:

```javascript
const API_URL =
  "https://vdojpubvf2.execute-api.ap-southeast-2.amazonaws.com/ApiDeploy/employees";
```

Update the endpoint if your API deployment changes.

Configure CORS to allow the exact CloudFront frontend origin. Ensure the API and Lambda responses return the appropriate CORS headers, including the required methods and headers. Redeploy API Gateway after configuration changes when necessary.

### Step 7: Test the Application

1. Open the CloudFront URL.
2. Submit an employee record through the web form.
3. Verify that the record appears in the employee list.
4. Check the item in DynamoDB.
5. Test the GET endpoint.
6. Review Lambda logs in CloudWatch if errors occur.
7. Check browser developer tools for API and CORS errors.

## Security Best Practices

- Keep the S3 bucket private and use CloudFront OAC.
- Apply least-privilege IAM permissions.
- Prefer separate execution roles for GetFunction and InsertFunction.
- Configure CORS for the exact frontend origin.
- Avoid exposing credentials, secrets, or personal data in the repository.
- Enable appropriate CloudWatch logs and monitoring.
- Consider API throttling and AWS WAF for applicable public entry points.

## Monitoring and Optional Enhancements

The following are potential improvements and should be marked as implemented only after configuration:

- AWS WAF for CloudFront or API Gateway, depending on the protected entry point.
- Amazon Route 53 for a custom domain.
- AWS Certificate Manager (ACM) for a custom-domain TLS certificate.
- CloudWatch alarms for Lambda errors and API failures.
- AWS CloudTrail for auditing AWS API activity.
- Amazon SNS for monitoring notifications.
- AWS CloudFormation for repeatable infrastructure deployment.

**WAF note:** A Web ACL associated with CloudFront protects traffic through that distribution. It does not automatically protect direct requests to the API Gateway `execute-api` endpoint. API protection requires a regional WAF association with API Gateway or routing API traffic through CloudFront.

## What I Learned

Gained hands-on experience with serverless architecture, REST API development, Python-based Lambda functions, NoSQL database integration, secure frontend delivery using a private S3 bucket and CloudFront OAC, IAM permissions, CORS configuration, and troubleshooting AWS deployments.

## Author

**Abutalha Parkote**

GitHub: https://github.com/Abutalha2132

## Disclaimer

This project is intended for educational and portfolio purposes. Production deployments should include appropriate authentication, authorization, input validation, data protection, monitoring, and security controls.
