#!/usr/bin/python3
def rconvert(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return 0


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    result = 0
    rlen = len(roman_string)
    for i in range(rlen):
        vcurrent = rconvert(roman_string[i])
        if (i < rlen - 1):
            vnext = rconvert(roman_string[i+1])
            result += vcurrent if vcurrent >= vnext else -vcurrent
        else:
            result += vcurrent
    return result
