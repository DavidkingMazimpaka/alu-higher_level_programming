#!/usr/bin/python3
"""
Sending a request to the URL and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    url_to_request = sys.argv[1]
    request_file = requests.get(url_to_request)
    print(request_file.headers.get('x-request-id'))
