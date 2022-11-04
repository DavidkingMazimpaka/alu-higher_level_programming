#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    add_list = list()
    if len(roman_string) == 1:
        return roman_numbers[roman_string]
    if len(roman_string) > 1:
        for i in range(0, len(roman_string)):
            try:
                if roman_string[i] == "I" and \
                        (roman_string[i + 1] == "V" or
                         roman_string[i + 1] == "X") \
                        or roman_string[i] == "X" and \
                        (roman_string[i + 1] == "C" or
                         roman_string[i + 1] == "L") \
                        or roman_string[i] == "C" and \
                        (roman_string[i + 1] == "D" or
                         roman_string[i + 1] == "M"):
                    add_list.append(-int(roman_numbers[roman_string[i]]))
                else:
                    add_list.append(int(roman_numbers[roman_string[i]]))
            except IndexError:
                add_list.append(int(roman_numbers[roman_string[i]]))
                pass
    return sum(add_list)
