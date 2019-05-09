#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary):
        print("{:s}: {}".format(x, a_dictionary[x]))
