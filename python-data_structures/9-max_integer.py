#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        if len(my_list) == 1:
            return my_list[0]
        else:
            action1 = my_list[0]
            action2 = max_integer(my_list[1:])
            if action1 > action2:
                return action1
            else:
                return action2
