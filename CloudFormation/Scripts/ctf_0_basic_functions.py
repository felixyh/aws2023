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
            delete_stack(stack_name, region=region)
            print('等待五秒删除处于\'ROLLBACK_COMPLETE\'状态的Stack')
            time.sleep(5)
            return False
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'DELETE_IN_PROGRESS':
            return True
    return False


def update_stack(stack_name, region='us-east-2'):
    pass



def delete_stack(stack_name, region='us-east-2'):
    client = boto3.client('cloudformation', region_name=region)
    response = client.delete_stack(
        StackName=stack_name,
    )
    return response
