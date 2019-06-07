#!/usr/bin/python3
"""Function to write a string to  a text file (UTF8)"""


def write_file(filename="", text=""):
    """Writes a string to a text file, returns number of chars written

    Args:
    filename (str): String containing filename.
    text     (str): String containing text to write to file

    Returns:
    Number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
