#!/usr/bin/python3
""" Square Module """

Rectangle = __import__('9-rectangle').Rectangle

class Square (Rectangle):
    """ Square Class inheriths from Rectangle.
    Instantiation with size
    """
    def __init__(self, size):
        """ Constructor.
        Size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string """
        return "[Square] {}/{}".format(self.__size, self.__size)
