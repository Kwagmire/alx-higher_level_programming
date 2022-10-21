#!/usr/bin/python3
"""Task 2 of ALX Project(Python - Network #1)

This script displays the body of the response
    to the POST request sent with a given piece of data
    to a given URL
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    value = sys.argv[2]
    values = {'email': value}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode('utf-8')))
