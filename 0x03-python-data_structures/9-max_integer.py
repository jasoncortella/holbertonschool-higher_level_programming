#!/usr/bin/python3
def max_integer(my_list=[]):
    maxret = 0
    for i in my_list:
        if i > maxret:
            maxret = i
    return maxret if my_list else None
