#!/usr/bin/python3
"""
A python file that has a function with division of all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    a function that divides the elements of a matrix by a divider
    """
    global matrix_rowSize
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        else:
            matrix_rowSize = len(matrix[0])

    """ Handling the exceptions in the file"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if len(matrix) == 0 or matrix == []:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if matrix is None:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) != matrix_rowSize:
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    """Creating new Matrix"""
    return list(map
                (lambda a: list(map(
                    lambda b: round(b / div, 2), a
                )), matrix))
