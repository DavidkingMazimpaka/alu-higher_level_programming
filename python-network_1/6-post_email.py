#!/usr/bin/python3
"""
Sending a post request with an email
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    test_file = {'email': sys.argv[2]}
    request_doc = requests.post(url, data=test_file)
    print(request_doc.text)