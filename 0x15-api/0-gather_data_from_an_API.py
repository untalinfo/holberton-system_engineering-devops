#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":

    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    list_task = []

    user_id = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(argv[1]))
    EMPLOYEE_NAME = requests.get(user_id).json()
    print("Employee {} is done with tasks"
          .format(EMPLOYEE_NAME.get('name')), end="")
    TASK = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for todo in TASK:
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                list_task.append(todo.get("title"))
    print('({}/{})'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for t in list_task:
        print('\t {}'.format(t))
