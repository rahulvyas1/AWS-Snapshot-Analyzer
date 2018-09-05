# AWS-Snapshot-Analyzer
Using Boto3 Python 3 library to Manage EC2 Instance snapshots

**This project will help manage your snapshots.**
1. Lists all your EC2 Instances:white_check_mark: :100:
2. Lists your Volumes 
3. Automatically create snapshots from your EC2 Volumes
4. Filter EC2 Instances using project name ( --project="YOUR PROJECT NAME ) :100: :white_check_mark:
5. Start & Stop Instances :100: :white_check_mark:

## Instructions to Run the program

### Install libraries
```python
pip3 install boto3
pip3 install click
```

### Configuring

shotty uses AWS configuration file created using the aws-cli, please follow the steps to configure your file-

`aws configure`

### Running

After doing the above steps you are good to run this program-

`python3 run pycode.py`

(OPTIONAL) To pass on a project as an argument please use this-

`python3 run pycode.py --project=YOUR_PROJECT_NAME`

*command* is list, start, or stop
*project* is optional
