#!/usr/bin/python3
"""
 a function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    returning error message with executables
    :param text:
    :return:
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    te = text.replace('.', '.\n\n')
    te = te.replace(':', ':\n\n')
    te = te.replace('?', '?\n\n')
    te = te.replace('\n ', '\n')
    print(te)
