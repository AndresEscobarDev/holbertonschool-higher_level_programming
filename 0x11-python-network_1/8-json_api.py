#!/usr/bin/python3
""" Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """


if __name__ == "__main__":
    import requests
    import sys

    q = ""
    if len(sys.argv) == 2:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        v = r.json()
        if len(v) > 0:
            print("[{}] {}".format(v.get('id'), v.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")