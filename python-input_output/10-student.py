#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON output."""


class Student:
    """A class that defines a student with filtered serialization."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary of Student, filtered by attrs if provided."""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__
