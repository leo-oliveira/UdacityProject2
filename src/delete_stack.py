import sys
import boto3
import json

cf_client = boto3.client('cloudformation')

def main(stack_name,):

    try:
        response = cf_client.delete_stack(
            StackName= stack_name
        )

        if 'ResponseMetadata' in response and \
            response['ResponseMetadata']['HTTPStatusCode'] < 300:
            print("succeed. response: {0}".format(json.dumps(response)))
        else:
            print("There was an Unexpected error. response: {0}".format(json.dumps(response)))

    except NameError as ex:
        print(ex)

if __name__ == '__main__':
    main(*sys.argv[1:])
