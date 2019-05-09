#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_keys.append(key)
    for x in delete_keys:
        del a_dictionary[x]
    return a_dictionary
