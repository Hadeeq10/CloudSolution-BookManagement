import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

def delete_item(book_id):
    """Delete a single item by book_id."""
    logger.info(f"Attempting to delete item with book_id: {book_id}")
    response = table.delete_item(Key={'book_id': book_id})
    
    if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
        logger.info(f"Item with book_id {book_id} deleted successfully")
    else:
        logger.warning(f"Failed to delete item with book_id {book_id}")

def lambda_handler(event, context):
    try:
        
        book_id = event['pathParameters']['id']  
        
        if not book_id:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
                },
                'body': json.dumps({'message': 'No book_id provided'})
            }

        
        response = table.get_item(Key={'book_id': book_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
                },
                'body': json.dumps({'message': f'Item with book_id {book_id} not found'})
            }
        
        
        delete_item(book_id)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'message': f'Item with book_id {book_id} deleted successfully'})
        }
    except Exception as e:
        logger.error(f"Error deleting item: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'message': 'Error deleting item', 'error': str(e)})
        }
