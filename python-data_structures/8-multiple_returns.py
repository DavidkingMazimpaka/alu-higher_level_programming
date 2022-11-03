#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        1st_letter = sentence[0]
    else:
        length = 0
        1st_letter = None
    return tuple((length, 1st_letter))
