#!/usr/bin/python3
""" Fetching data from an API """


import json
import sys
import urllib.request


def to_json():
    """ Request Function """
    emp_todo = {}
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"
    row = {}
    with urllib.request.urlopen(todo_url) as response:
        todo_json = json.loads(response.read())
    with urllib.request.urlopen(user_url) as res:
        user_json = json.loads(res.read())
    for todos in todo_json:
        emp_todo[todos['userId']] = []
        for user in user_json:
            row["task"] = todos['title']
            row["completed"] = todos['completed']
            row["username"] = user['username']
            emp_todo[todos['userId']].append(row)
    json_ = json.dumps(emp_todo)
    with open("todo_all_employees.json", 'w') as file:
        file.write(json_)


if __name__ == "__main__":
    to_json()
