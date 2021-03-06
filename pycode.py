import boto3
import click
ec2 = boto3.resource('ec2')


def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name':'tag:Project', 'Values':["Valkyrie"]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances

@click.group()
def cli():
    """Shotty manages snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@cli.group('instances')
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 Instances"
    instances = filter_instances(project)
    for i in instances:    
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>'))))
        #print(i)
        print(i.tags)

@instances.command('stop')
@click.option('--project', default=None,
help="Only instances for project")
def stop_instances(project):
    "Stop EC2 Instances"
    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()


@instances.command('start')
@click.option('--project', default=None,
help="Only instances for project")
def start_instances(project):
    "Start EC2 Instances"
    instances = filter_instances(project)
    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()


cli()