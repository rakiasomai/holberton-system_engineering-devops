#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
'''
import csv
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
            tmp = []
            tmp.extend((em_id,
                        username,
                        task.get("completed"),
                        task.get("title")))
            all.append(tmp)

    with open("{}.csv".format(em_id), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all)
