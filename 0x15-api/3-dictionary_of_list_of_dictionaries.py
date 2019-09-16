#!/usr/bin/python3
"""This extends the Python script in task 0 to export data for all employees
in JSON format"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    task_dict = {}
    for user in r:
        task_list = []
        user_id = user.get('id')
        username = user.get('username')
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos/?userId={:}'.format(
                user_id)).json()
        for item in todos:
            task = {}
            task["username"] = username
            task["task"] = item.get('title')
            task["completed"] = item.get('completed')
            task_list.append(task)
        task_dict[user_id] = task_list
    with open("todo_all_employees.json", 'w') as f:
        json.dump(task_dict, f)
