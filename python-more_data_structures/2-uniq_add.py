#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    add_int = 0
    for i in uniq_int:
        add_int += i
    return add_int