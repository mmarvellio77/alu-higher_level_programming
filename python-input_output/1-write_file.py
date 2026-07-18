#!/usr/bin/python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes text to a file and returns number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
