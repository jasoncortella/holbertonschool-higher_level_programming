#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    print("{} argument{}".format(a, ':' if a == 1 else 's:' if a else 's.'))
    for x in range(1, a + 1):
        print("{}: {}".format(x, argv[x]))
