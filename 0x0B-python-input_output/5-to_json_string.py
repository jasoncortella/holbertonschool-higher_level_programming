#!/usr/bin/python3
"""Function to return the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
    my_obj (obj): the object to process

    Returns:
    JSON representation of my_obj
    """
    return json.dumps(my_obj)
