import json
import boto3
from decimal import Decimal


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o) 
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        
        response = table.scan()
        books = response['Items']  

        
        for book in books:
            if 'book_id' not in book:
                print(f"Warning: Missing book_id for book {book}")
        
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  
                'Access-Control-Allow-Headers': 'Content-Type',  
                'Access-Control-Allow-Methods': 'OPTIONS,GET',  
            },
            'body': json.dumps(books, cls=DecimalEncoder)  
        }
    except Exception as e:
        
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,GET',
            },
            'body': json.dumps({'message': 'Error fetching books', 'error': str(e)})
        }
