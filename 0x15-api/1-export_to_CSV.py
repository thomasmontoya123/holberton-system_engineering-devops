#!/usr/bin/python3
'''Export to CSV'''
import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url_users = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
        response_users = requests.get(url_users)
        name = response_users.json().get('username')

        url_todos = 'https://jsonplaceholder.typicode.com/todos'
        response_todos = requests.get(url_todos)

        tasks = []
        for task in response_todos.json():
            if task.get('userId') == int(argv[1]):
                tasks.append(task)

        with open('{}.csv'.format(argv[1]), 'w') as f:
            fields = ["userId", "name", "completed", "title"]
            csv_write = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
            for task in tasks:
                task['name'] = name
                del task['id']
                csv_write.writerow(task)
