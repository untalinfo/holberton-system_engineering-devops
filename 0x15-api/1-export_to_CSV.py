#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    USER_ID = argv[1]
    file_name = USER_ID + '.csv'

    user_id = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(argv[1]))
    EMPLOYEE_NAME = requests.get(user_id).json()
    TASK = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    with open(file_name, mode='w', newline='') as csv_file:
        cvs_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for todo in TASK:
            if todo.get('userId') == int(USER_ID):
                cvs_writer.writerow([todo.get("userId"), EMPLOYEE_NAME.get
                                     ("username"), todo.get("completed"), todo.get
                                     ("title")])
