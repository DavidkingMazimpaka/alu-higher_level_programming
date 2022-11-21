#!/usr/bin/python3
"""
Taking a request and sending to URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
