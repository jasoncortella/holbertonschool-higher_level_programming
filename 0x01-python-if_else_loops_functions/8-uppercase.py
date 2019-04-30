#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = c
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            x = ord(c) - 32
        else:
            x = ord(c)
        print("{:c}".format(x), end='')
    print("")
