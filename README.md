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

- Goto DynamoDB
- Create table "sms_messages" with primary key "sid"
![alt tag](./img/config-dynamo-1.png)
- Create table "voice_calls" with primary key "sid"

# Lambda Configuration

- Goto Lambda Functions
- Create a lamba function "SMSMessageHandler" with runtime "Python 2.7" and template "Blank"
- Please select the DynamoDB role you created
![alt tag](./img/config-lambda-3.png)
- Add the following code to the inline editor
![alt tag](./img/config-lambda-2.png)
* code available in resources/lambda_functions/sms_message_handler.py
- Create a lambda function "VoiceCallHandler" with runtime "Python 2.7" and template "Blank"
- Add the following code to the inline editor
![alt tag](./img/config-lambda-3.png)
* code available in resources/lambda_functions/voice_call_handler.py

# API Gateway Configuration

- Goto API Gateway
- Create a new API labeled "TwilioBackend"
![alt tag](./img/config-api-1.png)
- Goto Actions -> Create Resource
- Create a resource for SMS Messages
![alt tag](./img/config-api-2.png)
- Click the "/smsmessage" endpoint
![alt tag](./img/config-api-3.png)
- Goto Actions -> Create Method
- Please select "POST"
- Please use Lambda Function "SMSMessageHandler"
![alt tag](./img/config-api-4.png)
- Click Save
- Goto "Integration Request"
![alt tag](./img/config-api-5.png)
- Click "Body Mapping Templates"
- Add a template for "application/x-www-form-urlencoded"
![alt tag](./img/config-api-6.png)
- For the template contents please use
![alt tag](./img/config-api-7.png)
* code available in resources/api_gateway_templates/endpoint_body_mapper.json
- Click Save
- Goto "Integration Response"
![alt tag](./img/config-api-11.png)
- Click "Body Mapping Templates"
- Please create a default mapping of "application/xml" and make the content blank
![alt tag](./img/config-api-12.png)
- Goto Actions -> Create Resource
- Create a resource for Voice Calls
![alt tag](./img/config-api-8.png)
* Please make sure you create the resource under the "/" root endpoint
- Click the "/voicecall" endpoint
- Goto Actions -> Create Method
- Please select "POST"
- Please use Lambda Function "VoiceCallHandler"
- Please setup the "Integration Request" the same as "SMSMessageHandler"
- Goto Actions -> "Deploy API"
- Please use a deployment stage or create one
![alt tag](./img/config-api-9.png)
- Click "Deploy"
- Copy the "Invoke URL"
![alt tag](./img/config-api-10.png)
* You will need to use endpoints "/smsmessage" and "/voicecall" so your
endpoints will need to look like:

SMS Messages
```
https://oo0tgkx9t1.execute-api.us-west-2.amazonaws.com/development/smsmessage
```

Voice Calls
```
https://oo0tgkx9t1.execute-api.us-west-2.amazonaws.com/development/voicecall
```

# Twilio Configuration 

- Please goto Phone Numbers
- Please click into a Phone Number
- Configure "Voice & Fax" with Incoming URL
![alt tag](./img/config-twilio-1.png)
- Configure "Messaging" with Incoming URL
![alt tag](./img/config-twilio-2.png)
- Click "Save"

# Testing

To test please send an SMS message or Call the Twilio number
used. The logs will be available in "AWS CloudWatch". You
should receive entries in your DynamoDB if everything is setup
correctly

Example of Lambda DB entry
![alt tag](./img/config-test-1.png)

