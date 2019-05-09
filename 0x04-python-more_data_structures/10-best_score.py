#!/usr/bin/python3
def best_score(a_dictionary):
    retval = 0
    retkey = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > retval:
                retval = value
                retkey = key
    return retkey
