#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function that adds two integers, casting floats to
integers first.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: First number, must be an integer or float.
        b: Second number, must be an integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b, cast to integers if float.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
