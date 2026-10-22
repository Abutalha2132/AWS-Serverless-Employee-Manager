# AWS-Serverless-Project
# AWS Serverless Employee Manager

A serverless employee management application built using AWS services. The application allows users to add employee details and retrieve employee records through a web interface connected to a REST API.

## Project Overview

The **AWS Serverless Employee Manager** demonstrates how to build and deploy a serverless web application using AWS managed services. It uses a static frontend, API Gateway for API requests, AWS Lambda for backend processing, and Amazon DynamoDB for data storage.

The project also provides practical experience with IAM permissions, CORS configuration, CloudFront distribution, and serverless application deployment.

## Architecture

![AWS Serverless Employee Manager Architecture](architecture.png)

### Architecture Workflow

1. Users access the web application through Amazon CloudFront.
2. Amazon S3 stores the static frontend files.
3. Amazon API Gateway receives HTTP requests from the frontend.
4. AWS Lambda executes backend logic for inserting and retrieving employee records.
5. Amazon DynamoDB stores employee information.
6. AWS IAM controls access to AWS resources.
7. Amazon CloudWatch can be used to monitor Lambda execution and troubleshoot errors.

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Stores frontend HTML, CSS, and JavaScript files |
| Amazon CloudFront | Delivers the frontend securely and efficiently |
| Amazon API Gateway | Exposes REST API endpoints |
| AWS Lambda | Executes backend Python code without managing servers |
| Amazon DynamoDB | Stores employee records in a NoSQL database |
| AWS IAM | Manages permissions for Lambda and other AWS resources |
| Amazon CloudWatch | Supports logging, monitoring, and troubleshooting |

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Cloud Platform:** Amazon Web Services (AWS)
- **API:** Amazon API Gateway REST API
- **Database:** Amazon DynamoDB
- **Delivery:** Amazon CloudFront and Amazon S3

## Application Features

- Add employee records through a web form.
- Retrieve and display employee records.
- Store employee information in Amazon DynamoDB.
- Use separate Lambda functions for insert and retrieve operations.
- Connect the frontend to backend services using API Gateway.
- Handle API responses and display employee information in the interface.
- Configure CORS to allow requests from the hosted frontend.

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
│
├── architecture.png
└── README.md
```

*Adjust the filenames in this structure to match the actual files in your repository.*

## DynamoDB Configuration

**Table name:** `employeeData`

**Partition key:** `employeeid`

**Key type:** String

The table stores employee information such as:

- `employeeid`
- `name`
- `email`
- `department`
- `salary`

The `employeeid` field uniquely identifies an employee record.

## Lambda Functions

### 1. GetFunction

Responsible for retrieving employee records from DynamoDB.

Responsibilities:
- Read employee data from the DynamoDB table.
- Return records in JSON format.
- Support retrieving all employees or a specific employee when implemented with an `employeeid` query parameter.
- Return appropriate HTTP responses and CORS headers.

### 2. InsertFunction

Responsible for inserting new employee records into DynamoDB.

Responsibilities:
- Read employee details from the API request body.
- Validate required fields.
- Insert employee records into DynamoDB.
- Reject duplicate employee IDs when the conditional write is configured.
- Return appropriate HTTP responses and CORS headers.

## API Configuration

The application uses an API Gateway REST API with the `/employees` resource.

| HTTP Method | Operation |
|---|---|
| `GET` | Retrieve employee records |
| `POST` | Insert a new employee record |
| `OPTIONS` | Handle browser CORS preflight requests |

**API endpoint:**

```text
https://vdojpubvf2.execute-api.ap-southeast-2.amazonaws.com/ApiDeploy/employees
```

The endpoint above is specific to the deployed project. Replace it if you recreate the application in another AWS account or region.

## Deployment Guide

### Step 1: Create the DynamoDB Table

1. Open the Amazon DynamoDB console.
2. Create a table named `employeeData`.
3. Set `employeeid` as the partition key.
4. Choose the String data type.
5. Create the table.

### Step 2: Create the Lambda Functions

1. Open the AWS Lambda console.
2. Create `GetFunction` using Python.
3. Add the retrieval code.
4. Create `InsertFunction` using Python.
5. Add the insertion code.
6. Configure the appropriate IAM execution permissions for DynamoDB and CloudWatch Logs.

### Step 3: Configure API Gateway

1. Create or configure a REST API.
2. Create the `/employees` resource.
3. Configure the `GET` method to invoke `GetFunction`.
4. Configure the `POST` method to invoke `InsertFunction`.
5. Configure the `OPTIONS` method and CORS headers.
6. Deploy the API to the `ApiDeploy` stage.

### Step 4: Host the Frontend on S3

1. Create an S3 bucket for the frontend.
2. Upload the HTML, CSS, and JavaScript files.
3. Configure access using the intended hosting architecture.
4. For a production deployment, keep the S3 bucket private and use CloudFront with Origin Access Control (OAC).

### Step 5: Configure CloudFront

1. Create a CloudFront distribution with the S3 bucket as its origin.
2. Configure the S3 origin using OAC.
3. Set `index.html` as the default root object.
4. Wait for the distribution to deploy.
5. Access the application using the CloudFront distribution domain.

### Step 6: Connect the Frontend to API Gateway

Configure the API endpoint in the frontend JavaScript:

```javascript
const API_URL =
  "https://vdojpubvf2.execute-api.ap-southeast-2.amazonaws.com/ApiDeploy/employees";
```

Update the URL if your API endpoint is different.

Configure CORS in API Gateway and the Lambda responses to allow the exact origin of your frontend. Redeploy the API after making changes to API Gateway configuration.

### Step 7: Test the Application

1. Open the application using the CloudFront URL.
2. Submit a new employee record.
3. Check whether the record appears in the employee list.
4. Verify the item in DynamoDB.
5. Check Lambda logs in CloudWatch if an error occurs.
6. Test the GET endpoint independently to verify record retrieval.

## Security and Best Practices

- Follow the principle of least privilege for IAM permissions.
- Prefer separate IAM execution roles for the two Lambda functions.
- Keep the S3 bucket private and use CloudFront OAC.
- Configure API Gateway CORS with the correct frontend origin.
- Enable CloudWatch logging and useful monitoring alarms.
- Consider API throttling and AWS WAF protection for applicable entry points.
- Avoid storing AWS credentials or sensitive information in the repository.
- Do not commit real employee data or secrets.

## Future Enhancements

- Add employee update and delete operations.
- Add input validation and improved error handling.
- Introduce pagination for large employee datasets.
- Configure a custom domain using Amazon Route 53.
- Add CloudWatch alarms and Amazon SNS notifications.
- Use AWS WAF to protect supported public entry points.
- Automate deployment using AWS CloudFormation or CI/CD pipelines.

## Learning Outcomes

Through this project, I gained practical experience with:

- Building a serverless application on AWS.
- Creating and configuring Lambda functions using Python.
- Integrating API Gateway with Lambda.
- Storing and retrieving records using DynamoDB.
- Hosting static websites on S3 and distributing content through CloudFront.
- Configuring IAM permissions and API CORS.
- Troubleshooting API requests, Lambda execution, and database operations.

## Author

**Abutalha Parkote**

GitHub: [Abutalha2132](https://github.com/Abutalha2132)

## Disclaimer

This project is intended for learning and demonstration purposes. Before using it in production, implement appropriate authentication, authorization, data protection, validation, monitoring, and security controls.
