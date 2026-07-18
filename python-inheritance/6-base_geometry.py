#!/usr/bin/python3
"""Module that defines BaseGeometry with an area method."""


class BaseGeometry:
    """A base geometry class with unimplemented area method."""

    def area(self):
        """Raises an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
