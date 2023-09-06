#!/usr/bin/python3
"""dividing a matrix"""


def matrix_divided(matrix, div):
    """divide elements of matrix by div

    Args:
        matrix: matrix of numbers
        div: number to divide matrix elements by

    Raises:
        TypeError: if matrix elements are not int or float
        TypeError: matrix rows are not the same size
        TypeError: div is not a number
        ZeroDivisionError: Dividing by zero

    Return:
        division result
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
#if div == 0:
#raise ZeroDivisionError("division by zero")
    if not isinstance (matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
