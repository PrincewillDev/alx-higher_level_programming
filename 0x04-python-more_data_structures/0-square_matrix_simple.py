#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(n)
        new_matrix.append(new_row)
    new_matrix = [[n**2 for n in row]for row in new_matrix]
    return (new_matrix)
