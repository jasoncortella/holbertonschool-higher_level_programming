#!/usr/bin/python3


def text_indentation(text):

    """
    text_indentation - prints a text with 2 new lines after
                     - each of these characters: ., ? and :

    *** There should be no space at the beginning
        or at the end of each printed line  ***

    Args:
        text: The text to be parsed and printed

    Returns:
        Always None

    Raises:
        - TypeError if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skipspaces = True
    for c in text:
        if c == ' ' and skipspaces is True:
            continue
        skipspaces = False
        if all(c != x for x in ('.', '?', ':')):
            print(c, end='')
        else:
            print(c, end='\n\n')
            skipspaces = True
