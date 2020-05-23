#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""
    def test_values(self):
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)
        self.assertEqual(max_integer([-3, 2, -1, 0]), 2)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([-56, 1, -564911]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
