#!/usr/bin/python3
"""
Fetching the url from the server
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as reply:
        body = reply.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode(encoding="utf -8")))
