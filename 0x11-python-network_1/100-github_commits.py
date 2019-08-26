#!/usr/bin/python3
"""Lists 10 most recent commits of a specified GitHub account"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
            commits[i].get("commit").get("author").get("name")))
