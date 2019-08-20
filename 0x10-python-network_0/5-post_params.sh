#!/bin/bash
# takes in URL, sends POST request to passed URL, displays body
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
