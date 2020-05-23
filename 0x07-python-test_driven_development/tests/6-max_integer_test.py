#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""
    def test_values(self):
        """Test diferent calues in the function"""
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)
        self.assertEqual(max_integer([-3, 2, -1, 0]), 2)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([-56.6, 1.7, -564911]), 1.7)
        self.assertEqual(max_integer([916]), 916)
        self.assertEqual(max_integer("123456789"), "9")
        self.assertEqual(max_integer(["hi", "hello"]), "hi")
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertRaises(TypeError, max_integer, 4)
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, ["a", "b", 8])

if __name__ == "__main__":
    unittest.main()
