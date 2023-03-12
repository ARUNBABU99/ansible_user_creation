#!/usr/bin/python3
import yaml
import os

with open("users.yml") as file:
    # parse the YAML file
    data = yaml.safe_load(file)
    users = data['users']
    for user in users:
        x=(user["name"])
        print("name" , x)
        a_path = "credentials"
        a_file = "password.txt"
        joined_path = os.path.join(a_path, x , a_file)
        f= open(f"{joined_path}", 'r')
        content = f. read().rstrip()
        print("pasword is" , content)
        a_path = "credentials"
        a_file = "passphrase.txt"
        joined_path = os.path.join(a_path, x , a_file)
        f= open(f"{joined_path}", 'r')
        content = f. read().rstrip()
        print("passphrase is" , content)
        print("\n")
        print("\n")
