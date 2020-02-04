#!/usr/bin/python3
'''Gather data from an API'''
from sys import argv
import json
import requests


if __name__ == "__main__":
    if len(argv) == 2:
        users_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
        users_response = requests.get(users_url)
        users_dictionary = json.loads(users_response.text)
        get_name_user = users_dictionary.get('name')

        todo_url = "https://jsonplaceholder.typicode.com/todos/?userId="\
            + argv[1]
        todo_response = requests.get(todo_url)
        tasks = json.loads(todo_response.text)
        completed_tasks = []

        for task in tasks:
            if task.get('completed'):
                completed_tasks.append(task)

        print("Employee {} is done with tasks({}/{}):".
              format(get_name_user, len(completed_tasks), len(tasks)))

        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))
