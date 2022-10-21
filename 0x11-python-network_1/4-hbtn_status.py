#!/usr/bin/python3
"""Task 4 of ALX Project(Python - Network #1)

This script fetches `https:alx-intranet.hbtn.io/status` using requests
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
