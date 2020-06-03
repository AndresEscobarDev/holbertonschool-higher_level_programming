#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry ():
    """ Class BaseGeometry.
    Public instance method: def area(self)
    Public instance method: def integer_validator(self, name, value)
    """
    def area(self):
        """ Method that raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
