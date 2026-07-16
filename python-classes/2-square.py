#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """A class that defines a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initializes a new Square with an optional size, default 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
