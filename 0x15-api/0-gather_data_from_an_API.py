#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID
'''
import requests
import sys

if __name__ == "__main__":
    em_id = sys.argv[1]
    name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(em_id)).json().get("name")
    total = 0
    done = []
    y = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in y:
        if (task.get("userId") == int(em_id)):
            total += 1
            if (task.get("completed")):
                done.append(task.get("title"))

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(name, len(done), total))

    for z in done:
        print("\t {}".format(z))
