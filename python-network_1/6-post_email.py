#!/usr/bin/python3
""" Sending a post request with an email """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    test_url_email = {'email': sys.argv[2]}
    request_file = requests.post(url, data=test_url_email)
    print(request_file.text)
