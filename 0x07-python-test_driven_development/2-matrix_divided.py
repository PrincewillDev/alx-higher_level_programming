#!/usr/bin/python3

"""
Divides all element of a matrix
Parameters: matrix, div
Returns: a new matrix of all divided elements
"""


def matrix_divided(matrix, div):
    """
    Divide all element of a matrix
    Return a new list with the divided elements
    """
    first_row = len(matrix[0])
    new_list = []

    # Check if matrix is a list of lists
    if type(matrix) is not list or len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    # Checks of rows are list type
    if not all(type(rw) is list for rw in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    # Check if all elements in matrix are int or float
    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if not isinstance(div, (int, float)):
        """ Raise TypeError if element of div is not int,float"""
        raise TypeError("div must be a number")

    for index in matrix:
        if len(index) != first_row:
            """ Raise TypeError if size of row is unequal """
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        """ Raise ZeroDivisionError if div is equal 0"""
        raise TypeError("division by zero")

    for row in matrix:
        new_row = []
        for column in row:
            result = round((column / div), 2)
            new_row.append(result)
        new_list.append(new_row)
    return new_list
