#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    """send the email"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code <= 400:
        print("{}".format(response.text))
    else:
        print("Error code: {}".format(response.status_code))

