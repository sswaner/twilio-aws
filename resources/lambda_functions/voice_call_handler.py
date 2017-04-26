import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    logger.info("RECEIVED EVENT: %s"%( str( event )) )
    params = event['params']
    sid = params['CallSid']
    from_number = params['From']
    to_number = params['To']
    logger.info("RECEIVED CALL SID: %s, FROM: %s, TO: %s" % ( sid, from_number, to_number ))
    client = boto3.client('dynamodb')
    client.put_item(TableName="voice_calls", Item={
         "sid": {'S': sid },
         "from": {'S': from_number },
         "to": {'S': to_number },
      })
    return ""

