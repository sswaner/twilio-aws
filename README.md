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

- Create table "sms_messages"
![alt tag](./img/config-dynamo-1.png)
**Please make "sid" the primary key**
- Create table "voice_calls"
![alt tag](./img/config-dynamo-1.png)
**Please also make "sid" the primary key**

# Lambda Configuration

- Create a lamdba function "SMSMessageHandler"
![alt tag](./img/config-lambda-1.png)
Please select runtime "Python 2.7" and the IAM role you created
**Click Save**
- Add the following code to the inline editor
![alt tag](./img/config-lambda-2.png)
*code available in resources/lambda_functions/sms_message_handler.py*
- Create a lambda function "VoiceCallHandler" 
Please select the same runtime and IAM role as "SMSMessageHandler"
**Click Save**
- Add the following code to the inline editor
![alt tag](./img/config-lambda-3.png)
*code available in resources/lambda_functions/voice_call_handler.py*

# API Gateway Configuration

- Create a new API labeled "TwilioBackend"
![alt tag](./img/config-api-1.png)
# Creating the "/smsmessage" resource
- Please click "Actions" -> "Create Resource"
![alt tag](./img/config-api-13.png)
- Please use "SMSMessage" for the resource name
![alt tag](./img/config-api-2.png)
- Click the "/smsmessage" endpoint
![alt tag](./img/config-api-3.png)
- Please click "Actions" -> "Create Method"
**Select method POST**
You will need to pick the lambda function you created earlier.
![alt tag](./img/config-api-4.png)
*Use use Lambda Function "SMSMessageHandler"*
**Click Save**
- Goto "Integration Request"
![alt tag](./img/config-api-5.png)
*Click "Body Mapping Templates'*
*Add a template for "application/x-www-form-urlencoded"*
![alt tag](./img/config-api-6.png)
- Add the following code to the textbox
![alt tag](./img/config-api-7.png)
*code available in resources/api_gateway_templates/endpoint_body_mapper.json*
**Click Save**
- Goto "Integration Response"
![alt tag](./img/config-api-11.png)
*Click "Body Mapping Templates"*
*Add a template for 'application/xml'. Please make the body blan*
![alt tag](./img/config-api-12.png)

# Creating the "/voicecall" resource
**Please make sure you create the resource under the "/" root endpoint**
![alt tag](./img/config-api-14.png)
- Please click "Actions" -> "Create Resource"
- Please use "VoiceCall" for the resource name
![alt tag](./img/config-api-15.png)
- Click the "/voicecall" endpoint
- Please click "Actions" -> "Create Method"
- Please select "POST"
- Please use Lambda Function "VoiceCallHandler"
- Please setup the "Integration Request" the same as "SMSMessageHandler"
- Please setup the "Integration Response" the same as "SMSMessageHandler"
# Deploying API
- Please click "Actions" -> "Deploy API"
![alt tag](./img/config-api-9.png)
*Please use a deployment stage or create one*
**Click Deploy**
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

- Login to Twilio
- Please go to "Phone Numbers" and click the phone number
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

