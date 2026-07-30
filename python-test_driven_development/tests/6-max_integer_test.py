#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with a list of integers in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of integers in random order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_reversed_list(self):
        """Test with a list of integers in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -1]), 5)

    def test_all_same(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_at_beginning(self):
        """Test with the max at the beginning."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test with the max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 0.5]), 3.1)

    def test_mixed_ints_floats(self):
        """Test with a mix of ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2.9]), 3)

    def test_large_list(self):
        """Test with a large list of numbers."""
        self.assertEqual(max_integer(list(range(1000))), 999)


if __name__ == '__main__':
    unittest.main()
