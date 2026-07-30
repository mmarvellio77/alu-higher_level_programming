#!/usr/bin/python3
"""Base class for managing id attribute."""

import json


class Base:
    """Base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.

        Args:
            id: If provided, assign to id attr. Otherwise increment
                __nb_objects and assign new value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = [o.to_dictionary() for o in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Return list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                dict_list = cls.from_json_string(f.read())
            return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
