#!/usr/bin/python3
"""This extends the Python script in task 0 to export data in CSV format"""
import csv
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                     .format(argv[1])).json()
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'
        .format(argv[1])).json()
    user_id = argv[1]
    user_name = r.get('username')
    with open('{:}.csv'.format(argv[1]), mode='w') as user_id_file:
        user_id_writer = csv.writer(user_id_file, quoting=csv.QUOTE_ALL)
        for task in r2:
            user_id_writer.writerow([user_id, user_name, task.get('completed'),
                                     task.get('title')])
