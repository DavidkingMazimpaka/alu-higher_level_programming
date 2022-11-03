#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        a = 0
        for i in j:
            if a == (len(j) - 1):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
            a += 1
        print("")
