import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

filters = [
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]

response = ec2.describe_instances(Filters=filters)

print("Running EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        public_ip = instance.get('PublicIpAddress', 'N/A')
        private_ip = instance.get('PrivateIpAddress', 'N/A')
        state = instance['State']['Name']
        az = instance['Placement']['AvailabilityZone']

        print(f'Instance ID: {instance_id}')
        print(f'  Type: {instance_type}')
        print(f'  Public IP: {public_ip}')
        print(f'  Private IP: {private_ip}')
        print(f'  State: {state}')
        print(f'  Availability Zone: {az}')
        print('---')
