#!/usr/bin/python3
"""Module that defines divisible_by_2"""


def divisible_by_2(my_list=[]):
    """Returns a list of booleans indicating if each integer is divisible by 2"""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
