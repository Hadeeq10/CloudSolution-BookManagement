import json
import boto3
from decimal import Decimal
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
       
        book_id = event['pathParameters']['id']
        
        
        book = json.loads(event['body'])
        
        required_fields = ['Title', 'Authors', 'Publisher', 'Year']
        missing_fields = [field for field in required_fields if field not in book]

        if missing_fields:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,PUT'
                },
                'body': json.dumps({'message': f'Missing required fields: {", ".join(missing_fields)}'})
            }

    
        response = table.update_item(
            Key={'book_id': book_id},
            UpdateExpression='SET #Title = :Title, #Authors = :Authors, #Publisher = :Publisher, #Year = :Year',
            ConditionExpression='attribute_exists(book_id)',
            ExpressionAttributeNames={
                '#Title': 'Title',
                '#Authors': 'Authors',
                '#Publisher': 'Publisher',
                '#Year': 'Year'
            },
            ExpressionAttributeValues={
                ':Title': book['Title'],
                ':Authors': book['Authors'],
                ':Publisher': book['Publisher'],
                ':Year': int(book['Year'])
            },
            ReturnValues='ALL_NEW'
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'message': 'Book updated successfully', 'item': response['Attributes']}, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'message': 'Error updating book', 'error': str(e)})
        }
