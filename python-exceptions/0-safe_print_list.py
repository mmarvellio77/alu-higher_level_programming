#!/usr/bin/python3
"""Module that defines safe_print_list"""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list, returns the number actually printed"""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
