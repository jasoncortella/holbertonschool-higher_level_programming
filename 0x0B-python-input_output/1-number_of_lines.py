#!/usr/bin/python3
"""Function to read a text file (UTF8) and count the number of lines in it"""


def number_of_lines(filename=""):
    """Reads a text file and returns the number of lines in it

    Args:
    filename (str): String containing filename.

    Returns:
    Nothing.
    """
    with open(filename, encoding="utf-8") as myFile:
        lineCount = 0
        for line in myFile:
            lineCount += 1
        return lineCount
