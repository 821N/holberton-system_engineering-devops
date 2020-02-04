#!/usr/bin/python3
"""
    1. Export to CSV
"""
import requests
from sys import argv
from json import loads


def get(path):
    response = requests.get("https://jsonplaceholder.typicode.com/"+path)
    return loads(response.text)

id = argv[1]
with open(id+".csv", "w") as file:
    user = get("users/"+id)
    todos = get("todos?userId="+id)
    for item in todos:
        file.write('"{}","{}","{}","{}"\n'.format(
            id, user['name'], item['completed'], item['title']
        ))
