#!/usr/bin/python3
""" Unittest Square Module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestSquare(unittest.TestCase):
    """ Test class for Square class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        s1 = Square(8)
        self.assertEqual(s1.id, 1)
        s2 = Square(6)
        self.assertEqual(s2.id, 2)
        s3 = Square(4, 0, 0, 99)
        self.assertEqual(s3.id, 99)
        s4 = Square(2, 4, 5)
        self.assertEqual(s4.id, 3)

    def test_atrs_and_args(self):
        r1 = Square(5, 7, 8, 9)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 9)
        r2 = Square(5, 7, 8)
        self.assertEqual(r2.size, 5)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.id, 1)
        r3 = Square(99)
        self.assertEqual(r3.size, 99)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 2)
        with self.assertRaises(TypeError) as e:
            Square("8")
        self.assertTrue("width must be an integer" in str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(-8)
        self.assertTrue("width must be > 0" in str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(8, "10")
        self.assertTrue("x must be an integer" in str(e.exception))
        with self.assertRaises(TypeError) as e:
            Square(8, 10, [11])
        self.assertTrue("y must be an integer" in str(e.exception))

    def test_area(self):
        r1 = Square(8)
        self.assertEqual(r1.area(), 64)
        r2 = Square(10, 12, 13, 14)
        self.assertEqual(r2.area(), 100)
