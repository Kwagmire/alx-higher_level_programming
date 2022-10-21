#!/usr/bin/python3
"""Task 3 of ALX Project(Python - Network #1)

This script displays the body of the response
    to a request to a given URL. It handles
    HTTPError exceptions
"""


if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.read()
            print("{}".format(content.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
