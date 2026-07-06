#!/usr/bin/python3
"""Module that removes all 'c' and 'C' characters from a string."""


def no_c(my_string):
    """Returns a new string with all 'c' and 'C' characters removed."""
    return "".join([ch for ch in my_string if ch != 'c' and ch != 'C'])
