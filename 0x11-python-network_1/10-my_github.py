#!/usr/bin/python3
"""displays GitHub ID based on credentials using GitHub API"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    x = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=x)
    print(r.json().get("id"))
