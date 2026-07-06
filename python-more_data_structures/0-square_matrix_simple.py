#!/usr/bin/python3
"""Module that defines square_matrix_simple"""


def square_matrix_simple(matrix=[]):
    """Returns a new matrix with each value squared"""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
