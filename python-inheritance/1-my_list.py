#!/usr/bin/python3
"""Module that defines MyList, a subclass of list."""


class MyList(list):
    """A class that inherits from list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
