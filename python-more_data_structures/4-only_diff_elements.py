#!/usr/bin/python3
"""Module that defines only_diff_elements"""


def only_diff_elements(set_1, set_2):
    """Returns a set of elements present in only one of the two sets"""
    return set_1 ^ set_2
