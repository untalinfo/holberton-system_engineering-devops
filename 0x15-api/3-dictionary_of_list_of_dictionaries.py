#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    file_name = 'todo_all_employees.json'

    USERS = requests.get('https://jsonplaceholder.typicode.com/users').json()
    TASK = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    data = {}

    for user in USERS:
        task = []
        data[user.get('id')] = []
        for todo in TASK:
            if todo.get('userId') == user.get('id'):
                data[user.get('id')].append({"username": user.get("username"),
                                             "task": todo.get("title"),
                                             "completed": todo.get("completed")
                                             })

    with open(file_name, mode='w') as json_file:
        json.dump(data, json_file)
