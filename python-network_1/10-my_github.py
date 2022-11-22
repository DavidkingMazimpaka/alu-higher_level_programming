#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def searchapi():
    """
    returning the status
    :return:
    """
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(username, password)))

    try:
        data = result.json()
        print(data["id"])
    except:
        print("None")


if __name__ == "__main__":
    searchapi()
