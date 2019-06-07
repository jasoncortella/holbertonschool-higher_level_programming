#!/usr/bin/python3
"""Function to read a text file (UTF8) and print it to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
    filename (str): String containing filename.

    Returns:
    Nothing.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
