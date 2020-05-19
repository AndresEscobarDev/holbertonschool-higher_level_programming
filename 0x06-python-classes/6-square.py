#!/usr/bin/python3
"""Square Module"""


class Square():
    """Square.
    Private instance attribute: size:
        property def size(self).
        property setter def size(self, value).
    Private instance attribute: position:
        property def position(self).
        property setter def position(self, value).
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """"prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        print("".join("\n" for j in range(self.__position[1])), end="")
        for i in range(self.__size):
            print("".join(" " for j in range(self.__position[0])), end="")
            print("".join("#" for j in range(self.__size)), end="")
            print("\n" if i + 1 != self.__size else "", end="")
        print()
