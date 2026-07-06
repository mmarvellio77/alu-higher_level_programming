#!/usr/bin/python3
"""Module that defines max_integer"""


def max_integer(my_list=[]):
    """Returns the biggest integer in a list, or None if list is empty"""
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest
