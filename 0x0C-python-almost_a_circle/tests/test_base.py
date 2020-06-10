#!/usr/bin/python3
""" Unittest base Module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """ Test class for Base class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_creating_an_instance(self):
        instance = Base()
        self.assertIsInstance(instance, Base)

    def test_nb_objects_exists(self):
        b = Base()
        self.assertTrue(hasattr(b, 'id'))

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(99)
        self.assertEqual(b3.id, 99)
        b4 = Base()
        self.assertEqual(b4.id, 3)
