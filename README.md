# twilio-aws

What you will need

```
AWS Account
Twilio Account
```


AWS Services you will need

```
Lambda Functions
DynamoDB
API Gateway
IAM
CloudWatch
```

# IAM Configuration 
Please enable access for Lambda and DynamoDB. This can be
done in your IAM roles. For more information please view: http://docs.aws.amazon.com/lambda/latest/dg/with-dynamodb-create-execution-role.html


# DynamoDB Configuration

You will need to create two tables "sms_messages" and "voice_calls".
Please follow the steps below to configure DynamoDB correctly.

- Create a table "sms_messages"
![alt tag](./img/config-dynamo-1.png)
*Please make "sid" the primary key and click 'Create'*

- Create another table "voice_calls"

*Please make the primary key "sid", the same as "sms_messages" and click "Create"*

## When your tables are created. DynamoDB should look like
![alt tag](./img/config-dynamo-4.png)

# Lambda Configuration

You will need two Lambda functions. One for incoming SMS,
and one for incoming calls. The steps below create two
handlers. Please follow the steps to setup your Lambda
functions correctly.

- Create a lambda function
![alt tag](./img/config-lambda-4.png)
*Please use "Python 2.7" as the runtime, and click "Blank Function"*

*You will need to setup "triggers". Please click "Next" at this step*

- Configure the lamdba function.
![alt tag](./img/config-lambda-1.png)
*Please use "SMSMessageHandler" as the name, select runtime "Python 2.7" and the IAM role you created. 
Then click "Save"*

## In the following screen you will need to edit the function.

- Add the following code to the inline editor
![alt tag](./img/config-lambda-2.png)
*code available in resources/lambda_functions/sms_message_handler.py*

## Creating the "VoiceCallHandler"
*Please create another function and title this function "VoiceCallHandler" then repeat the same steps as "SMSMessageHandler'*

## In the editor screen

- Add the following code to the inline editor

![alt tag](./img/config-lambda-3.png)
*code available in resources/lambda_functions/voice_call_handler.py*

- Please save all changes

# API Gateway Configuration

We need one API. This will be used for both calls and SMS. Please
follow the steps below to create the API.

- Create a new API
![alt tag](./img/config-api-16.png)
![alt tag](./img/config-api-1.png)
*Please select "New API" and use "TwilioBackend" as the "API Name"*

# Creating the "/smsmessage" resource
- Please click "Actions" -> "Create Resource"
![alt tag](./img/config-api-13.png)

- Please use "SMSMessage" for the resource name
![alt tag](./img/config-api-2.png)

- Click the "/smsmessage" endpoint
![alt tag](./img/config-api-3.png)

- Please create a "POST" method. Click "Actions" -> "Create Method"
![alt tag](./img/config-api-17.png)

![alt tag](./img/config-api-18.png)
*Use Lambda Function "SMSMessageHandler" and click "Save"*

- Please goto "Integration Request"
![alt tag](./img/config-api-5.png)

## You will need to add a "Body Mapping Template'
- Please create a template for "application/x-www-form-urlencoded"
![alt tag](./img/config-api-6.png)
*Please select 'Never' for 'Request body passthrough*

- Add the following code to the textbox and save
![alt tag](./img/config-api-7.png)
*code available in resources/api_gateway_templates/endpoint_body_mapper.json*

- Please goto "Integration Response"
![alt tag](./img/config-api-11.png)
## You will need to add another 'Body Mapping Template'
- Please create a template for "application/xml"
![alt tag](./img/config-api-12.png)
*Please keep this template blank and save*

# Creating the "/voicecall" resource

*Please make sure you create the resource under the "/" root endpoint*

![alt tag](./img/config-api-14.png)
- Please click "Actions" -> "Create Resource"

![alt tag](./img/config-api-15.png)

*Please create a "POST" method for this endpoint*

# Deploying API

- Please click "Actions" -> "Deploy API"

![alt tag](./img/config-api-9.png)

*Please use a deployment stage or create one*

- Click "Deploy"

- Copy the "Invoke URL"
![alt tag](./img/config-api-10.png)

*You will need to use endpoints "/smsmessage" and "/voicecall" so your
endpoints will need to look like:*

SMS Messages
```
https://oo0tgkx9t1.execute-api.us-west-2.amazonaws.com/development/smsmessage
```

Voice Calls
```
https://oo0tgkx9t1.execute-api.us-west-2.amazonaws.com/development/voicecall
```

# Twilio Configuration 

The Twilio account will need to be assigned the webhooks we copied
from the AWS API Gateway. Please follow these steps to setup
the Twilio.

- Please go to your "Twilio Console"

- Please go to "Phone Numbers" and click this phone number

- Configure "Voice & Fax" with Incoming URL
![alt tag](./img/config-twilio-1.png)

- Configure "Messaging" with Incoming URL
![alt tag](./img/config-twilio-2.png)

- Click "Save"

# Testing

To test please send an SMS message or Call the Twilio number
used. The logs will be available in "AWS CloudWatch" and "Twilio Debugger". You
should receive entries in your DynamoDB if everything is setup
correctly.

*Example of Lambda DB entry*
![alt tag](./img/config-test-1.png)

