#!/usr/bin/python3
""" Fetching data from an API """


import csv
import json
import sys
import urllib.request


def to_csv():
    """ Request Function """
    id = sys.argv[1]
    emp_todo = []
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/" + id
    e_nam = ""
    rows = []
    with urllib.request.urlopen(todo_url) as response:
        todo_json = json.loads(response.read())
    with urllib.request.urlopen(user_url) as res:
        user_json = json.loads(res.read())
    e_nam = user_json['name']
    for todos in todo_json:
        if todos['userId'] == int(id):
            emp_todo.append(todos)
    for tod in emp_todo:
        title = tod['title']
        comp = tod['completed']
        un = user_json['username']
        row = '"{}", "{}", "{}", "{}"'.format(id, un, comp, title)
        rows.append(row)
    with open(id+".csv", 'w', newline='') as file:
        w = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=" ")
        for row1 in rows:
            w.writerow([row1])


if __name__ == "__main__":
    to_csv()
