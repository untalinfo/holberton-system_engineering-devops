#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    USER_ID = argv[1]
    file_name = USER_ID + '.json'

    user_id = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(argv[1]))
    EMPLOYEE_NAME = requests.get(user_id).json()
    TASK = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    data = {}
    data[USER_ID] = []

    for todo in TASK:
        if todo.get('userId') == int(USER_ID):
            data[USER_ID].append({"task": todo.get("title"),
                                  "completed": todo.get("completed"),
                                  "username":
                                  EMPLOYEE_NAME.get("username")})

    with open(file_name, mode='w') as json_file:
        json.dump(data, json_file)
