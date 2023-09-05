#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len,matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(i / div, 2) for i in row] for row in matrix]
    return result
