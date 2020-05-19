#!/usr/bin/python3
"""Square Module"""


class Square():
    """Square.
    Private instance attribute: size:
        property def size(self).
        property setter def size(self, value).
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(self.__size):
            print("".join("#" for j in range(self.__size)), end="")
            print("\n" if i + 1 != self.__size else "", end="")
        print()
