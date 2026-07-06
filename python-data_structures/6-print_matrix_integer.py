#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers, one row per line, space-separated."""
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
