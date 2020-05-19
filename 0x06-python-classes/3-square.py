#!/usr/bin/python3
class Square():
    """Square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2
