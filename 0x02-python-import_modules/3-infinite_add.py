#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = 0
    b = len(argv) - 1
    for x in range(b):
        a += int(argv[x + 1])
    print(a)
