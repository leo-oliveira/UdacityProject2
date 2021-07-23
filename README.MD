# Project 2: Deploy a high-availability web app using CloudFormation

## Introduction

This repo mains to exercise the knowledge acquired in the course `Cloud DevOps Engineer Nanodegree Program`, module 3: `Deploy Infrastructure as Code (IAC)`

## Infrastructure diagram

![Diagram that represents the infrastructure develop in the CloudFormation script](/docs/images/project2.png)

## Helpers scripts

Before using any helper script the necessary python requirements must be installed. The command below does it:

`pip3 install -r requirements.txt`

### Create or update stack

[create_update_stack.py](/src/create_update_stack.py) creates or updates a stack.

Parameters:

`stack_name`: name of the stack
`template`: resources yml template
`parameters`: json paramaters for the template

#### How to run the script

python3 .\create_update_stack.py "stack_name" template parameter

`python3 .\create_update_stack.py "UdacityProject2" .\network.yml .\network-parameters.json`

### Delete stack

[delete_stack.py](/src/delete_stack.py) deletes a stack.

Parameters:

`stack_name`: name of the stack

#### How to run the script

python3 .\delete_stack.py "stack_name"

`python3 .\delete_stack.py "UdacityProject2"`

### Running the project

1 - Install the python requirements:

- `pip3 install -r requirements.txt`

 2 - Run the network template in order to create the network infrastructure in AWS:

- `python3 .\create_update_stack.py "UdacityProject2" .\network.yml .\network-parameters.json`

 3 - Run the servers template in order to create the necessary resources in AWS:

 - `python3 .\create_update_stack.py "servers" .\servers.yml .\servers-parameters.json`

