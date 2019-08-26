#!/usr/bin/python3
"""takes in URL and email, sends POST request to email, displays response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    req = requests.post(url, data=values)
    print(req.text)
