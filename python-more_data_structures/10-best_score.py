#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        name = ''
        score = 0
        for value in a_dictionary:
            if a_dictionary[value] > score:
                name = value
                score = a_dictionary[value]
    return name
