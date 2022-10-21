#!/usr/bin/python3
"""Task 5 of ALX Project(Python - Network #1)

This script displays the value of the X-Request-Id variable
    found in the header of the response
    to the request sent to a given URL
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    print((response.headers).get('X-Request-Id'))
