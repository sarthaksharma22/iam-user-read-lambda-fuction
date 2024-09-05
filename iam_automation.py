import boto3
import yaml

# Initialize the IAM client
iam = boto3.client('iam')

def create_iam_user(username):
    try:
        iam.create_user(UserName=username)
        print(f"User {username} created successfully.")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User {username} already exists.")

def add_user_to_group(username, groupname):
    try:
        iam.add_user_to_group(UserName=username, GroupName=groupname)
        print(f"Added {username} to {groupname} group.")
    except Exception as e:
        print(f"Error adding {username} to {groupname}: {e}")

def process_users_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    for user in data['users']:
        username = user['username']
        groups = user['groups']
        
        # Create IAM user
        create_iam_user(username)

        # Add user to the specified groups
        for group in groups:
            add_user_to_group(username, group)

if __name__ == "__main__":
    yaml_file_path = "iam_users.yaml"
    process_users_from_yaml(yaml_file_path)
