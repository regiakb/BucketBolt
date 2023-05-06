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


1. List Buckets and their size
+-----------+-----------+
| Bucket    |    Size   |
+-----------+-----------+
| bucket1   | 535.03 GB |
| bucket2   | 548.18 MB |
+-----------+-----------+


2. List Users and their permissions
+------------------------------+----------------------+-------------------------------+
|    User                      |    Access Key ID     |             Policy            |
+------------------------------+----------------------+-------------------------------+
|   testbucketgithubUser1      | AKIATXXXXXXXXXXXXXXX |         AmazonS3FullAccess    |
|   testbucketgithubUser2      | AKIATXXXXXXXXXXXXXXX |          Bucket-bucket2       |
|   testbucketgithubUser3      | AKIATXXXXXXXXXXXXXXX |          Bucket-bucket1       |
+------------------------------+----------------------+-------------------------------+

3. Create new Bucket and Users

Bucket Name: testbucketgithub
Nº of users for this bucket: 3
Credentials saved on a .txt
+-----------------------+----------------------+------------------------------------------+
|        Usuario        |    Access Key ID     |            Secret Access Key             |
+-----------------------+----------------------+------------------------------------------+
| testbucketgithubUser1 | AKIATXXXXXXXXXXXX    |                  HIDDEN                  |
| testbucketgithubUser2 | AKIATXXXXXXXXXXXX    |                  HIDDEN                  |
| testbucketgithubUser3 | AKIATXXXXXXXXXXXX    |                  HIDDEN                  |
+-----------------------+----------------------+------------------------------------------+


4. Delete Bucket, policies, and Users

Buckets List:
testbucketgithub

Bucket Name to delete: testbucketgithub
Bucket testbucketgithub deleted.

testbucketgithubUser1 has not assigned this policy
Detached policy for user testbucketgithubUser1
Detached policy for user testbucketgithubUser2
Detached policy for user testbucketgithubUser3
Policy arn:aws:iam::<USER ID>:policy/Bucket_testbucketgithub removed.

User testbucketgithubUser1 removed.
User testbucketgithubUser2 removed.
User testbucketgithubUser3 removed.

Removal complete.

```
