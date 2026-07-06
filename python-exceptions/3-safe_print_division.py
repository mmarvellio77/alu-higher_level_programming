#!/usr/bin/python3
"""Module that defines safe_print_division"""


def safe_print_division(a, b):
    """Divides two integers and prints the result inside finally"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
