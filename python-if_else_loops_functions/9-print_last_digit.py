#!/usr/bin/python3
def print_last_digit(number):
    num_str = repr(number)
    last_num = num_str[-1]
    print(f"The last digit of {number} is {last_num}")
print_last_digit(2334)
