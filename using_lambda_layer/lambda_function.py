import json
from matrix_utils import transpose_matrix

def lambda_handler(event, context):
    # return transpose of a matrix
    matrix = event['matrix']
    print(matrix_utils.transpose_matrix(matrix))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
