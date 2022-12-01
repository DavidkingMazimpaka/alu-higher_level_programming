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
    if type(text) != str:
        raise TypeError('text must be a string')
    message = (':' + '\n\n').join([x.strip(" ") for x in text.split(':')])
    message = ('.' + '\n\n').join([y.strip(" ") for y in message.split('.')])
    message = ('?' + '\n\n').join([z.strip(" ") for z in message.split('?')])
    print(message, end="")
