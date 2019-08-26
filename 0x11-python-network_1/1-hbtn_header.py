#!/usr/bin/python3
"""takes in URL, sends request, displays value of X-Request-Id variable"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
