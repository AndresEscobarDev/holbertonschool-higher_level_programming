#!/usr/bin/python3
"""Square Module"""


class Square():
    """Square.
    Private instance attribute: size:
        property def size(self).
        property setter def size(self, value).
    Instantiation with optional size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    def __eq__(self, next):
        """Equal."""
        return self.__size == next

    def __ne__(self, next):
        """Diferent."""
        return self.__size != next

    def __lt__(self, next):
        """Less than."""
        return self.__size < next

    def __le__(self, next):
        """Less or equal than."""
        return self.__size <= next

    def __gt__(self, next):
        """Greater than."""
        return self.__size > next
    
    def __ge__(self, next):
        """Greater or equal than."""
        return self.__size >= next

    def area(self):
        """returns the current square area"""
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
