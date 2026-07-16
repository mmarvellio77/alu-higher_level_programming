#!/usr/bin/python3
"""Module that defines a Square class with a property getter and setter."""


class Square:
    """A class that defines a square with a property for size access."""

    def __init__(self, size=0):
        """Initializes a new Square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
