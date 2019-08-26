#!/usr/bin/python3
"""takes in URL, sends request, displays value of X-Request-Id variable"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('x-request-id'))
