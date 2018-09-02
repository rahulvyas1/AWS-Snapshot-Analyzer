import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)
#print(type(response))
#print(response['Reservations'][0]['Instances'][0]['InstanceId'])
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

def displayVolumes():
    for v in volumes:
        print(v)

#getVolumeOfInstance()
getAllVolumes()
displayVolumes()