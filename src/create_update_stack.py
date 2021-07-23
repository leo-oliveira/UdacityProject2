import sys
import boto3
import json

cf_client = boto3.client('cloudformation')

def main(stack_name, template, parameters):

    template_data = parse_template(template)
    parameter_data = parse_parameters(parameters)

    params = {
        'StackName': stack_name,
        'TemplateBody': template_data,
        'Parameters': parameter_data,
        'Capabilities':['CAPABILITY_NAMED_IAM']
    }

    try:
        if stack_exists(stack_name):
            print('Updating {}'.format(stack_name))
            cf_client.update_stack(**params)
            print('Stack {} updated successfully'.format(stack_name))
        else:
            print('Creating {}'.format(stack_name))
            cf_client.create_stack(**params)
            print('Stack {} created successfully'.format(stack_name))

    except NameError as ex:
        print(ex)
        # error_message = ex.response['Error']['Message']
        # if error_message == 'No updates are to be performed.':
        #     print("No changes")

def parse_template(template):
    with open(template) as template_fileobj:
        template_data = template_fileobj.read()
    cf_client.validate_template(TemplateBody=template_data)
    return template_data


def parse_parameters(parameters):
    with open(parameters) as parameter_fileobj:
        parameter_data = json.load(parameter_fileobj)
    return parameter_data


def stack_exists(stack_name):
    try:
        response = cf_client.describe_stacks(StackName = stack_name)
    except Exception:
        return False
    return True


if __name__ == '__main__':
    main(*sys.argv[1:])
