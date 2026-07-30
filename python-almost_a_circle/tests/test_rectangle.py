#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        """Test rectangle creation."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_full(self):
        """Test rectangle with all args."""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width_not_int(self):
        """Test width not int raises TypeError."""
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_height_not_int(self):
        """Test height not int raises TypeError."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_x_not_int(self):
        """Test x not int raises TypeError."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_not_int(self):
        """Test y not int raises TypeError."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_width_zero(self):
        """Test width <= 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_width_negative(self):
        """Test width < 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(-1, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_zero(self):
        """Test height <= 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 0)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_height_negative(self):
        """Test height < 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -1)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_negative(self):
        """Test x < 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negative(self):
        """Test y < 0 raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with large values."""
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        """Test __str__ with default x, y."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_no_xy(self):
        """Test display without x, y."""
        r = Rectangle(2, 2)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display with x, y."""
        r = Rectangle(2, 3, 2, 2)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), expected)

    def test_update_args_id(self):
        """Test update with args - id only."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        """Test update with all args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_skip_if_args(self):
        """Test kwargs are skipped if args exist."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        expected = {"id": r.id, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(d, expected)

    def test_width_setter_validation(self):
        """Test width setter validation."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter_validation(self):
        """Test height setter validation."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_setter_validation(self):
        """Test x setter validation."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter_validation(self):
        """Test y setter validation."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_bool_is_not_allowed(self):
        """Test bool is not allowed as int."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_update_kwargs_multiple(self):
        """Test update with multiple kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)

    def test_float_not_allowed(self):
        """Test float is not allowed."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)


if __name__ == "__main__":
    unittest.main()
