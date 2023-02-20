import boto3
import botocore
import time


def get_stack_status(stack_name, region='us-east-2'):
    client = boto3.client('cloudformation', region_name=region)
    response = client.list_stacks()

    for s in response.get('StackSummaries'):
        if s.get('StackName') == stack_name and s.get('StackStatus') == "CREATE_COMPLETE":
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'ROLLBACK_COMPLETE':
            