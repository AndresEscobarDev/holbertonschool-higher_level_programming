#!/usr/bin/python3
"""Magic Module"""
import math


class MagicClass():
    """MagicClass.
    Public instance attribute: _MagicClass__radius.
    Instantiation with optional radius.
    Public instance method: def area(self).
    Public instance method: def circumference(self).
    """
    def __init__(self, radius):
        """Constructor"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        _MagicClass__radius = radius

    def area(self):
        """returns the current circumference area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """returns circumference"""
        return 2 * math.pi * self._MagicClass__radius
