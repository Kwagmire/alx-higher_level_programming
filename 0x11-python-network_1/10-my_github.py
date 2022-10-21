#!/usr/bin/python3
"""Task 9 of ALX Project(Python - Network #1)

This script:
    - takes your GitHub credentials (username and password)
    - uses the GitHub API to display your id
"""


import sys
import requests

if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
