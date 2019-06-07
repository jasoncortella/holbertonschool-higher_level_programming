#!/usr/bin/python3
"""Function to insert a string into a text file (UTF8)"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
       a specific string

    Args:
    filename      (str): String containing filename.
    search_string (str): String containing text to define insertion point
    new_string    (str): String containing text to insert

    Returns:
    Nothing
    """
    newText = ""
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            newText += line
            if search_string in line:
                newText += new_string

    with open(filename, 'w', encoding="utf-8") as newFile:
        newFile.write(newText)
