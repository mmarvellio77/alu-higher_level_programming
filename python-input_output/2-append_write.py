#!/usr/bin/python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends text to a file and returns number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
