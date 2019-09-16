#!/usr/bin/python3
"""This extends the Python script in task 0 to export data in JSON format"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                     .format(argv[1])).json()
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'
        .format(argv[1])).json()
    user_id = argv[1]
    username = r.get('username')
    tasks = {}
    task_list = []
    for item in r2:
        task = {}
        task["task"] = item.get('title')
        task["completed"] = item.get('completed')
        task["username"] = username
        task_list.append(task)
    tasks[user_id] = task_list
    with open("{:}.json".format(user_id), 'w') as f:
        json.dump(tasks, f)
