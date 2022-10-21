#!/usr/bin/python3
"""Task 6 of ALX Project(Python - Network #1)

This script displays the body of the response
    to the POST request sent with a given piece of data
    to a given URL
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    value = sys.argv[2]
    values = {'email': value}
    response = requests.post(url, values)
    print(response.text)
