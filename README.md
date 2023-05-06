# BucketBolt - S3 Bucket Manage script
Python script for managing S3 buckets. Allows the creation and deletion of S3 buckets and users. Very easy to use.

This Python script uses the AWS boto3 library to create, list, and delete S3 buckets. It also lists IAM users and their access keys, and can create users with access permissions to a specific bucket.

To run this code, you need AWS credentials with appropriate permissions to create and delete S3 buckets, list IAM users, and their attached policies. The code can be executed from the command line or from a script file.

## Options:

1. List Buckets and their size
2. List Users and their permissions
4. Create new Bucket and Users
    If bucket name is BUCKET_NAME, the users will be BUCKET_NAMEUser1, BUCKET_NAMEUser2, etc. 
    Policy will be Bucket_BUCKETNAME
4. Delete Bucket, policies, and Users
    Delete all, bucket, policies and users


## Dependencies

To install dependencies:

```python
pip install boto3 prettytable colorama
```

## Usage/Examples

```python
  ____                   _             _       ____            _   _
 |  _ \                 | |           | |     |  _ \          | | | |
 | |_) |  _   _    ___  | | __   ___  | |_    | |_) |   ___   | | | |_
 |  _ <  | | | |  / __| | |/ /  / _ \ | __|   |  _ <   / _ \  | | | __|
 | |_) | | |_| | | (__  |   <  |  __/ | |_    | |_) | | (_) | | | | |_
 |____/   \__,_|  \___| |_|\_\  \___|  \__|   |____/   \___/  |_|  \__|
                                                             by Regiakb
-----------------------
Select an option:
-----------------------
1. List Buckets and their size
2. List Users and their permissions
3. Create new Bucket and Users
4. Delete Bucket, policies, and Users
5. Exit
```
