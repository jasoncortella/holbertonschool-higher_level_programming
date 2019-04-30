#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        abnumber = -number
    else:
        abnumber = number
    lastdigit = abnumber % 10
    print("{}".format(lastdigit), end='')
    return lastdigit
