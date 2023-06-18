#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squeres = []
    for i in matrix:
        inside = list(map(lambda x: x**2, i))
        squeres.append(inside)
    return squeres
