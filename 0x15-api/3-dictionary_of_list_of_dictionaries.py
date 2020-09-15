#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    USER_ID = argv[1]
    file_name = 'todo_all_employees.json'

    USERS = requests.get('https://jsonplaceholder.typicode.com/users').json()
    TASK = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    data = {}

    for user in USERS:
        data[user.get('id')] = []
        for todo in TASK:
            data[user.get('id')].append({"task": todo.get("title"),
                                         "completed": todo.get("completed"),
                                         "username":
                                         user.get("username")})

    with open(file_name, mode='w') as json_file:
        json.dump(data, json_file)
