#!/usr/bin/python3
"""Module that defines safe_print_integer"""


def safe_print_integer(value):
    """Prints an integer using {:d} format, returns True if successful"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
