#!/usr/bin/python3
"""Function to append a string to the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Appends a string to end of a text file, returns number of chars written

    Args:
    filename (str): String containing filename.
    text     (str): String containing text to append to file

    Returns:
    Number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
