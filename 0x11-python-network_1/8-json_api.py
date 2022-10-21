#!/usr/bin/python3
"""Task 8 of ALX Project(Python - Network #1)

This script sends a POST request to http://0.0.0.0:5000/search_user and:
    - sends a given letter as the value of the variable 'q'
    - assigns "" to 'q' if no letter was specified
    - displays the response in a specified format
    - displays a specified message if the JSON is invalid or empty
"""


if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(sys.argv) > 1:
        data["q"] = sys.argv[1]

    response = requests.post(url, data)
    try:
        jSON = response.json()
        if jSON == {}:
            print("No result")
        else:
            print("[{}] {}".format(jSON.get("id"), jSON.get("name")))
    except Exception:
        print("Not a valid JSON")
