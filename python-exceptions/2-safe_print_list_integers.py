#!/usr/bin/python3
"""Module that defines safe_print_list_integers"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints only the integers among the first x elements of a list"""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
