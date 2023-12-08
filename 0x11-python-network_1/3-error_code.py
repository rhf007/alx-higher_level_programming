#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as res:
            page = res.read()
            print(page.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
