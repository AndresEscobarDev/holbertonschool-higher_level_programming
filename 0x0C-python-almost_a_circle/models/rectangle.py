#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class.
    Private instance attributes:
        __width, __height, __x, __y
    Public method area
    Public method display
    Public method update
    Public method to_dictionary
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.height * self.width

    def display(self):
        """ Prints in stdout the Rectangle
        instance with the character #
        """
        print("".join("\n" for j in range(self.y)), end="")
        for i in range(self.height):
            print("".join(" " for j in range(self.x)), end="")
            print("".join("#" for j in range(self.width)), end="")
            print("\n" if i + 1 != self.height else "", end="")
        print()

    def __str__(self):
        """ Representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Method that update all
        values of the rectangle
        """
        if args is not None and len(args) > 0:
            if type(args[0]) is not int and args[0] is not None:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                    if len(args) > 3:
                        self.x = args[3]
                        if len(args) > 4:
                            self.y = args[4]
        else:
            for i, j in kwargs.items():
                if i == "id":
                    if type(j) is not int and j is not None:
                        raise TypeError("id must be an integer")
                    self.id = j
                if i == "width":
                    self.width = j
                if i == "height":
                    self.height = j
                if i == "x":
                    self.x = j
                if i == "y":
                    self.y = j

    def to_dictionary(self):
        """ Method that returns the dictionary
        representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
