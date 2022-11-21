#!/usr/bin/python3
"""checks url body status"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request_file = requests.get(url)
    try:
        request_file.raise_for_status()
        print(request_file.text)
    except Exception as e:
        print("Error code: {}".format(request_file.status_code))
