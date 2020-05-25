#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle():
    """Empty Rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) not in [int, float]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) not in [int, float]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Create the string for the print statement"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.height):
            for i in range(self.width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes a Rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
