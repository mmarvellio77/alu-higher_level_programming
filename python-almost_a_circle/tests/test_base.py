#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_none(self):
        """Test id auto-increment when id is None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_provided(self):
        """Test id is set when provided."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_mixed(self):
        """Test mixed auto and provided ids."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with valid dict."""
        d = [{"id": 1, "width": 10}]
        result = Base.to_json_string(d)
        self.assertEqual(result, '[{"id": 1, "width": 10}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with valid string."""
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertEqual(result, [{"id": 1, "width": 10}])

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_valid(self):
        """Test save_to_file with valid list."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)
        self.assertIn("height", content)
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create with rectangle dictionary."""
        r1 = Rectangle(3, 5, 1)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create with square dictionary."""
        s1 = Square(5)
        d = s1.to_dictionary()
        s2 = Square.create(**d)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_valid(self):
        """Test load_from_file with valid file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
