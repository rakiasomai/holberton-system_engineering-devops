#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
'''
import json
import requests
import sys

if __name__ == "__main__":
    em_id = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(em_id)).json().get("username")
    all = []
    y = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in y:
        if (task.get("userId") == int(em_id)):
            tmp = {}
            tmp["task"] = task.get("title")
            tmp["completed"] = task.get("completed")
            tmp["username"] = username
            all.append(tmp)

    with open("{}.json".format(em_id), 'w+') as jsonfile:
        json.dump({em_id: all}, jsonfile)
