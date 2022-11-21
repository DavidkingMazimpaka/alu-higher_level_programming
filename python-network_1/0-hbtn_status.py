#!/usr/bin/python3
"""
This file checks and fetches the status of current url from the server
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as reply:
        body = reply.read()
    print("Status Response: ")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode(encoding="utf -8")))
