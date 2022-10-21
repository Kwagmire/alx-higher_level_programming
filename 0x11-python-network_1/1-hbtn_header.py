#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Network #1)

This script displays the value of the X-Request-Id variable
    found in the header of the response
    to the request sent to a given URL
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
