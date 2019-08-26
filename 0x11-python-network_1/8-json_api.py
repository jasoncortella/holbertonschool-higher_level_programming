#!/usr/bin/python3
"""takes in a letter, sends POST resuest with letter as parameter"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    payload = {"q": q}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        x = r.json()
        if len(x) == 0:
            print("No result")
        else:
            print("[{}] {}".format(x.get('id'), x.get('name')))
    except:
        print("Not a valid JSON")
