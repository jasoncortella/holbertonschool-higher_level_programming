#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
import requests
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    values = {"search": sys.argv[1]}
    results = requests.get(url, params=values)
    x = results.json()
    print("Number of results: {}".format(x.get("count")))
    for items in x.get("results"):
        print(items.get("name"))
        films = items.get("films")
        for film in films:
            results = requests.get(film)
            x = results.json()
            print("\t{}".format(x.get("title")))
    next_page = x.get('next')
    while next_page:
        results = requests.get(next_page)
        x = results.json()
        for item in x.get('results'):
            print(item.get('name'))
        for film in films:
            results = requests.get(film)
            x = results.json()
            print("\t{}".format(x.get("title")))
        next_page = x.get('next')
