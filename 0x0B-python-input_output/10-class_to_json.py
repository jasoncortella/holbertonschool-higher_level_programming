#!/usr/bin/python3
"""Function to return dict description for JSON serialization"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
       (list, dictionary, string, integer and boolean) for JSON
       serialization of an object:

    Args:
    obj (obj): Object to process

    Returns:
    Associated dictionary description
    """
    return obj.__dict__
