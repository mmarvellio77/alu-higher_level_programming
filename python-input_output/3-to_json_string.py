#!/usr/bin/python3
"""Module that returns JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Returns the JSON string representation of my_obj."""
    return json.dumps(my_obj)
