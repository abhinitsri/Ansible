#!/usr/bin/env python3

import boto3
import json

session = boto3.Session(
            aws_access_key_id='Your Access Key',
                aws_secret_access_key='Your Secret Access Key',
                    region_name='default-region'
                    )
def get_ec2_instances():
    ec2 = session.client('ec2', region_name='ap-south-1')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['PublicIpAddress'])
    return instances

def main():
    instances = get_ec2_instances()
    inventory = {"dynamic_inventory": {"hosts": instances}}
    print(json.dumps(inventory))

if __name__ == "__main__":
    main()
