import boto3
import click
ec2 = boto3.resource('ec2')

@click.command()
@click.option('--project', default=None,
help="Only instances for project (tag Project:<name>)")
def getAllEC2Instances(project):
    "List EC2 Instances"
    instances = []
    for i in ec2.instances.all():    
        print(i)


getAllEC2Instances()