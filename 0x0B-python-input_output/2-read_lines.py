#!/usr/bin/python3
"""Function to read n lines of a text file (UTF8) and print them to stdout"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file and prints it to stdout

    Args:
    filename (str): String containing filename.
    nb_lines (int): Integer containing number of lines to print

    Returns:
    Nothing.
    """
    with open(filename, encoding="utf-8") as myFile:
        lineCount = 0
        for line in myFile:
            if lineCount < nb_lines or nb_lines <= 0:
                print(line, end="")
            lineCount += 1
