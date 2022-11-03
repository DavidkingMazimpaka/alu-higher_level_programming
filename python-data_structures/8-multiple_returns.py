#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        fst_letter = sentence[0]
    else:
        length = 0
        fst_letter = None
    return tuple((length, fst_letter))
