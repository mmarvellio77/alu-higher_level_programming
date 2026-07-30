#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """Test square creation."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_full(self):
        """Test square with all args."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_size_getter(self):
        """Test size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_not_int(self):
        """Test size not int raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        """Test size <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        """Test size < 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_str(self):
        """Test __str__ method."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_full(self):
        """Test __str__ with all args."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display_no_xy(self):
        """Test display without x, y."""
        s = Square(2)
        output = StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display with x, y."""
        s = Square(2, 2, 1)
        output = StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        expected = "\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), expected)

    def test_update_args(self):
        """Test update with args."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(1, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_kwargs_skip_if_args(self):
        """Test kwargs are skipped if args exist."""
        s = Square(5)
        s.update(10, size=7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        expected = {"id": s.id, "size": 10, "x": 2, "y": 1}
        self.assertEqual(d, expected)

    def test_inherits_rectangle(self):
        """Test Square inherits from Rectangle."""
        s = Square(5)
        from models.rectangle import Rectangle
        self.assertIsInstance(s, Rectangle)

    def test_size_setter_negative(self):
        """Test size setter with negative raises ValueError."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_size_setter_not_int(self):
        """Test size setter with non-int raises TypeError."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "invalid"


if __name__ == "__main__":
    unittest.main()
