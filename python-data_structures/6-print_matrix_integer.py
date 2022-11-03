#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        if not j:
            print()
        else:
            for i in j:
                if i == j[-1]:
                    print("{:d}".format(i))
                else:
                    print('{:d}'.format(i), end=" ")
