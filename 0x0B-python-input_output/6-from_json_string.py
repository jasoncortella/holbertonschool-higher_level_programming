#!/usr/bin/python3
"""Function to return an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """returns the object represented by a JSON string)

    Args:
    my_str (str): the JSON string to process

    Returns:
    object represented by JSON string
    """
    return json.loads(my_str)
