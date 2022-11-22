#!/usr/bin/python3
""" Listing 10 commits """
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    print(url)
    commits = requests.get(url).json()

    for data in commits:
        print("{}: {}".format(data['sha'], data['author']['login']))
