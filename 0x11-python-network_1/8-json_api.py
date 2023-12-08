#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r.json()
        if len(r.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
