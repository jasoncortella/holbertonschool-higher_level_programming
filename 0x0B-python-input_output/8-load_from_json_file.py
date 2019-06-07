#!/usr/bin/python3
"""Function to create an object from a JSON file"""

import json


def load_from_json_file(filename):
    """creates object from JSON file)

    Args:
    filename (str): String containing filename

    Returns:
    Created object
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
