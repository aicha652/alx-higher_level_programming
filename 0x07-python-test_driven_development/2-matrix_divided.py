#!/usr/bin/python3
"""Create a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Define function that divides all elements of a matrix"""

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for row in matrix:
        for i in row:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return result
