import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    logger.info("RECEIVED EVENT: %s"%( str( event )) )
    params = event['params']
    sid = params['MessageSid']
    from_number = params['From']
    to_number = params['To']
    body = params['Body']
    logger.info("RECEIVED MESSAGE SID: %s, FROM: %s, TO: %s, BODY: %s" % ( sid, from_number, to_number, body))
    client = boto3.client('dynamodb')
    client.put_item(TableName="sms_messages", Item={
         "sid": {'S': sid},
         "from": {'S': from_number},
         "to": {'S': to_number},
         "body": {'S': body}})
    return ""
