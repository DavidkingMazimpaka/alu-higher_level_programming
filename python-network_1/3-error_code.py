#!/usr/bin/python3
"""
Send a request and retrieve display the body of the response with (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


def sender():
    """sender"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    sender()
