#!/usr/bin/python3
"""Function to write an object's JSON representation to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """returns the object represented by a JSON string)

    Args:
    my_obj   (obj): the object to process
    filename (str): String containing filename

    Returns:
    Nothing.
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
