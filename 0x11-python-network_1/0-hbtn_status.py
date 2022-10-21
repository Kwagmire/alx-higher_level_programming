#!/usr/bin/python3
"""Task 0 of ALX Project(Python - Network #1)

This script fetches `https:alx-intranet.hbtn.io/status` using urllib
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
