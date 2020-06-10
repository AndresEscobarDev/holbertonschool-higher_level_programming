#!/usr/bin/python3
""" Unittest rectangle Module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(8, 9)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(6, 7)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(4, 5, 0, 0, 99)
        self.assertEqual(r3.id, 99)
        r4 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r4.id, 3)

    def test_atrs_and_args(self):
        r1 = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 9)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.id, 1)
        r3 = Rectangle(99, 100)
        self.assertEqual(r3.width, 99)
        self.assertEqual(r3.height, 100)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle(8, "9")
        self.assertTrue("height must be an integer" in str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle("8", 9)
        self.assertTrue("width must be an integer" in str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(8, -9)
        self.assertTrue("height must be > 0" in str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(-8, 9)
        self.assertTrue("width must be > 0" in str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(8, 0)
        self.assertTrue("height must be > 0" in str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(8, 9, "10")
        self.assertTrue("x must be an integer" in str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(8, 9, 10, [11])
        self.assertTrue("y must be an integer" in str(e.exception))

    def test_area(self):
        r1 = Rectangle(8, 9)
        self.assertEqual(r1.area(), 72)
        r2 = Rectangle(10, 11, 12, 13, 14)
        self.assertEqual(r2.area(), 110)
