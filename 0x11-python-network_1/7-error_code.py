#!/usr/bin/python3
"""Task 7 of ALX Project(Python - Network #1)

This script displays the body of the response
    to a request to a given URL. It handles
    HTTPError exceptions
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
