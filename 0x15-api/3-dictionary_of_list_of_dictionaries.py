#!/usr/bin/python3
""" Fetching data from an API """


import json
import sys
import urllib.request


def to_json():
    """ Request Function """
    emp_todo ={}
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"
    e_nam = ""
    rows = {}
    row = {}
    with urllib.request.urlopen(todo_url) as response:
        todo_json = json.loads(response.read())
    with urllib.request.urlopen(user_url) as res:
        user_json = json.loads(res.read())
    for user in user_json:
        for todo in todos:
            if user['id'] = todo['userId']:
                emp_todo[user['id']] = todo
    """for todos in todo_json:
        emp_todo['userId'].append(todos)
    rows[str(id)] = []
    for tod in emp_todo:
        row["task"] = tod['title']
        row["completed"] = tod['completed']
        row["username"] = user_json['username']
        rows[str(id)].append(row)
    json_ = json.dumps(rows)
    with open("todo_all_employees.json", 'w') as file:
        file.write(json_)"""


if __name__ == "__main__":
    to_json()
