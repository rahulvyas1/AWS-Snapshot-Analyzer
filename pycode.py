import boto3
import click
ec2 = boto3.client('ec2')




response = ec2.describe_instances()

instanceId = response['Reservations'][0]['Instances'][0]['InstanceId']

blockDeviceMappings = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings']
#snapshot = ec2.create_snapshot(VolumeId='volume')
volumes = []


#print(response['Reservations'][1]['Instances'][0]['BlockDeviceMappings'])

def getAllVolumes():
    for reservation in response['Reservations']:
        for block_device_mapping in reservation['Instances'][0]['BlockDeviceMappings']:
            #print(block_device_mapping)
            volumes.append(block_device_mapping['Ebs']['VolumeId'])

@click.command()
def displayVolumes():
    "Display All AWS Volumes"
    for v in volumes:
        print(v)

def getAllEC2Instances():
    for reservation in response['Reservations']:
        for i in reservation['Instances']:
            print(i['InstanceId'])

#getVolumeOfInstance()
#getAllVolumes()
#displayVolumes()

getAllEC2Instances()