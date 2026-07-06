#!/usr/bin/python3
"""Module that defines uniq_add"""


def uniq_add(my_list=[]):
    """Adds all unique integers in a list, each counted only once"""
    unique_values = set(my_list)
    total = 0
    for value in unique_values:
        total += value
    return total
