#!/bin/bash
# sends a request URL and displays size of response's body
curl -s "$1" | wc -c
