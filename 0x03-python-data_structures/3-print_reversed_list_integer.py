#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list), 0, -1):
            print("{:d}".format(i))
