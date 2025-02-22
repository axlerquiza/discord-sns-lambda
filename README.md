# Discord SNS Lambda Integration

This project demonstrates how to integrate AWS Lambda with Discord webhooks using AWS SNS. The Lambda function listens for SNS notifications and sends the message to a Discord channel via a webhook.

## Project Structure

- **lambda/lambda_function.py**: The Python code for the AWS Lambda function that processes SNS messages and sends them to Discord.
- **lambda/requests-layer.zip**: The zipped layer that includes the `requests` library, which is used in the Lambda function to send HTTP requests to the Discord webhook.

## AWS Setup

### 1. Lambda Function

- The Lambda function is triggered by an SNS message.
- The function extracts the message from SNS and sends it to Discord using a webhook.

### 2. SNS

- An SNS topic is used to send the message to the Lambda function.

## How to Deploy

1. Create an AWS Lambda function.
2. Upload the **lambda_function.py** code to the Lambda function.
3. Create a Lambda Layer:
   - Upload the **requests-layer.zip** as a layer to your Lambda function.
4. Attach the created layer to your Lambda function.
5. Set the function's **trigger** to your SNS topic.

## Prerequisites

- AWS account with permissions to create Lambda functions, Layers, and SNS topics.
- A Discord webhook URL to send the message to.

## Usage

Once the Lambda function is set up and triggered by SNS, it will forward the SNS message to the specified Discord channel.
