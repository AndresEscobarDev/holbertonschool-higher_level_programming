#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class.
    Inherits from Rectangle
    Public instance attribute size
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Representation of the square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Retrieves the square size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size """
        super().update(width=value, height=value)

    def update(self, *args, **kwargs):
        """ Method that update all
        values of the square
        """
        if args is not None and len(args) > 0:
            if type(args[0]) is not int and args[0] is not None:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]
        else:
            for i, j in kwargs.items():
                if i == "id":
                    if type(j) is not int and j is not None:
                        raise TypeError("id must be an integer")
                    self.id = j
                if i == "size":
                    self.width = j
                if i == "x":
                    self.x = j
                if i == "y":
                    self.y = j

    def to_dictionary(self):
        """ Method that returns the dictionary
        representation of a Square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
