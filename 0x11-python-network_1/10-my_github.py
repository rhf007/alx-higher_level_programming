#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    ba = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=ba)
    uid = r.json().get("id")
    print(uid)
