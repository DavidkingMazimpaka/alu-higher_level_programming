#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for word in a_dictionary.copy():
        if a_dictionary[word] == value:
            a_dictionary.pop(word)
    return a_dictionary
