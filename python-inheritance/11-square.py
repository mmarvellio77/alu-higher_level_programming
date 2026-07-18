#!/usr/bin/python3
"""Module that defines Square with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class with [Square] string representation."""

    def __init__(self, size):
        """Initializes Square with a validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
