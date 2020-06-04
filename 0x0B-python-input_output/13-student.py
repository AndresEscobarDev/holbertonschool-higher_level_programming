#!/usr/bin/python3
""" Student Module """


class Student():
    """ Class Student
    Public instance attribute first_name
    Public instance attribute last_name
    Public instance attribute age
    Public method def to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that retrieves a dictionary
        representation of a Student instance
        """
        if type(attrs) == list and all(type(x) == str for x in attrs):
            new = {}
            for i in attrs:
                if i in self.__dict__:
                    new.update({i: self.__dict__[i]})
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """ Method that replaces all
        attributes of the Student instance
        """
        for i in json:
            self.__dict__.update({i: json[i]})
