import boto3
import math
import json
from prettytable import PrettyTable
from botocore.exceptions import ClientError
import colorama
from colorama import Fore, Back

colorama.init()

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name=''
)


print("  ____                   _             _       ____            _   _   ")
print(" |  _ \                 | |           | |     |  _ \          | | | |  ")
print(" | |_) |  _   _    ___  | | __   ___  | |_    | |_) |   ___   | | | |_ ")
print(" |  _ <  | | | |  / __| | |/ /  / _ \ | __|   |  _ <   / _ \  | | | __|")
print(" | |_) | | |_| | | (__  |   <  |  __/ | |_    | |_) | | (_) | | | | |_ ")
print(" |____/   \__,_|  \___| |_|\_\  \___|  \__|   |____/   \___/  |_|  \__|")
print("                                                             by Regiakb")

s3 = session.resource('s3')
iam = session.client('iam')

def create_bucket():
    bucket_name = input("Bucket's name: ")
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(Fore.GREEN + f"Bucket {bucket_name} successfully created!" + Fore.RESET)
    except ClientError as e:
        print(Fore.RED + str(e) + Fore.RESET)

def list_buckets():
    table = PrettyTable()
    table.field_names = ["Bucket", "Size"]

    for bucket in s3.buckets.all():
        size_bytes = sum(obj.size for obj in bucket.objects.all())
        size_mb = size_bytes / (1024 * 1024)
        if size_mb > 1024:
            size_gb = size_mb / 1024
            size_str = f"{math.ceil(size_gb * 100) / 100} GB"
        else:
            size_str = f"{math.ceil(size_mb * 100) / 100} MB"
        table.add_row([bucket.name, size_str])

    print(table)

def list_users():
    
    table = PrettyTable(['User', 'Access Key ID', 'Policy'])

    users = iam.list_users()['Users']

    for user in users:
        user_name = user['UserName']

        access_keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']

        for access_key in access_keys:
            access_key_id = access_key['AccessKeyId']

            policies = []
            attached_policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
            for policy in attached_policies:
                policy_arn = policy['PolicyArn']
                if '/' in policy_arn:
                    policy_name = policy_arn.split('/')[-1]
                    policies.append(policy_name)

            if len(policies) > 0:
                table.add_row([user_name, access_key_id, ', '.join(policies)])
    print(table)

def create_bucket_users():

    bucket_name = input("Enter the bucket name: ")

    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-3'})

    iam = session.client('iam')

    num_users = int(input("How many users you want? "))

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}",
                    f"arn:aws:s3:::{bucket_name}/*"
                ]
            }
        ]
    }

    policy_arn = iam.create_policy(
        PolicyName=f"Bucket_{bucket_name}",
        PolicyDocument=json.dumps(policy)
    )["Policy"]["Arn"]

    with open(f"{bucket_name}.txt", "w") as f:
        f.write(f"Nombre del Bucket: {bucket_name}\n\n")
        
        tabla = PrettyTable(["Usuario", "Access Key ID", "Secret Access Key"])
        
        for i in range(1, num_users + 1):
            user_name = f"{bucket_name}User{i}"
            user = iam.create_user(UserName=user_name)
            access_key = iam.create_access_key(UserName=user_name)["AccessKey"]
            iam.attach_user_policy(
                UserName=user_name,
                PolicyArn=policy_arn
            )
            
            tabla.add_row([user_name, access_key["AccessKeyId"], access_key["SecretAccessKey"]])
            
            f.write(f"Usuario: {user_name}\nAccess Key ID: {access_key['AccessKeyId']}\nSecret Access Key: {access_key['SecretAccessKey']}\n\n")
        print(Fore.GREEN + f"The credentials of the bucket: {bucket_name} have been saved in a txt" + Fore.RESET)
        print(tabla)

def delete_buckets():
    s3s = session.client('s3')
    response = s3s.list_buckets()
    buckets = response['Buckets']
    print("Buckets List:")
    for bucket in buckets:
        print(bucket['Name'])
    bucket_name = input("Name of bucket to delete: ")
    response = s3s.list_objects(Bucket=bucket_name)
    s3s.delete_bucket(Bucket=bucket_name)
    print(Fore.GREEN + f"Bucket {bucket_name} deleted." + Fore.RESET)
    policy_arn = f"arn:aws:iam::<USER ID>:policy/Bucket_{bucket_name}"

    response = iam.list_users()

    for user in response['Users']:
        try:
            iam.detach_user_policy(UserName=user['UserName'], PolicyArn=policy_arn)
            print(Fore.GREEN + f"Policy disassociated from user {user['UserName']}" + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"{user['UserName']} does not have this policy assigned" + Fore.RESET)

    iam.delete_policy(PolicyArn=policy_arn)
    print(Fore.GREEN + f"Policy {policy_arn} deleted." + Fore.RESET)
    users = iam.list_users()
    for user in users['Users']:
        if user['UserName'].startswith(bucket_name):
            access_keys = iam.list_access_keys(UserName=user['UserName'])
            for access_key in access_keys['AccessKeyMetadata']:
                iam.delete_access_key(UserName=user['UserName'], AccessKeyId=access_key['AccessKeyId'])
            iam.delete_user(UserName=user['UserName'])
            print(Fore.GREEN + f"User {user['UserName']} deleted." + Fore.RESET)

    print(Fore.GREEN + "Deletion completed." + Fore.RESET)



def menu():
    print("-----------------------")
    print("Select an option:")
    print("-----------------------")
    print("1. List Buckets and their size")
    print("2. List Users and their permissions")
    print("3. Create new Bucket and Users")
    print("4. Delete Bucket, policies, and Users")
    print("5. Exit")

while True:
    menu()
    option = input("Opción: ")
    if option == "1":
        list_buckets()
    elif option == "2":
        list_users()
    elif option == "3":
        create_bucket_users()
    elif option == "4":
        delete_buckets()
    elif option == "5":
        break
    else:
        print("That does not exist, try again")
