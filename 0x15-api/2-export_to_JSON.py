#!/usr/bin/python3
""" Fetching data from an API """


import json
import sys
import urllib.request


def to_json():
    """ Request Function """
    id = sys.argv[1]
    emp_todo = []
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/" + id
    e_nam = ""
    rows = {}
    row = {}
    with urllib.request.urlopen(todo_url) as response:
        todo_json = json.loads(response.read())
    with urllib.request.urlopen(user_url) as res:
        user_json = json.loads(res.read())
    e_nam = user_json['name']
    for todos in todo_json:
        if todos['userId'] == int(id):
            emp_todo.append(todos)
    rows[str(id)] = []
    for tod in emp_todo:
        row["task"] = tod['title']
        row["completed"] = tod['completed']
        row["username"] = user_json['username']
        rows[str(id)].append(row)
    json_ = json.dumps(rows)
    with open(id+".json", 'w') as file:
        file.write(json_)


if __name__ == "__main__":
    to_json()
