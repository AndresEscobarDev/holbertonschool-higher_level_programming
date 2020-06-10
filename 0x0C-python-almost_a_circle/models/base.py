#!/usr/bin/python3
""" Base Module """
import json
import csv


class Base:
    """ Class Base
    private class attribute __nb_objects
    public instance attribute id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if type(id) is not int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the
        JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) is not list \
                or not all(type(i) is dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method save_to_file that
        writes the JSON string representation
        of list_objs to a file
        """
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary()
                                           for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Static method from_json_string that
        returns the list of the JSON string
        representation json_string
        """
        if json_string is not None and json_string != "":
            if type(json_string) is not str:
                raise TypeError("json_string must be a string")
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Class method create that returns an
        instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method load_from_file that
        returns a list of instances
        """
        l = []
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                s = f.read()
                ld = cls.from_json_string(s)
                for i in ld:
                    l.append(cls.create(**i))
                return l
        except FileNotFoundError:
            return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Class methods save_to_file_csv
        that serializes in CSV
        """
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                l = [i.to_dictionary() for i in list_objs]
                if cls.__name__ == "Rectangle":
                    w = csv.DictWriter(f, fieldnames=['id', 'width',
                                                      'height', 'x', 'y'])
                elif cls.__name__ == "Square":
                    w = csv.DictWriter(f, fieldnames=['id', 'size', 'x', 'y'])
                w.writeheader()
                w.writerows(l)

    @classmethod
    def load_from_file_csv(cls):
        """ Class methods load_from_file_csv
        that deserializes in CSV
        """
        l = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                r = csv.reader(f, delimiter=',')
                if cls.__name__ == "Rectangle":
                    n = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    n = ['id', 'size', 'x', 'y']
                for i, row in enumerate(r):
                    if i > 0:
                        d = {}
                        for j, k in enumerate(row):
                            d.update({n[j]: int(k)})
                        l.append(cls.create(**d))
                return l
        except FileNotFoundError:
            return l

    """@staticmethod
    def draw(list_rectangles, list_squares):
         Static method draw that opens
        a window and draws all the Rectangles
        and Squares
        
        import turtle

        t = turtle.Turtle()
        turtle.bgcolor("purple")
        t.color("blue")
        t.shape("Square")
        t.pensize(10)
        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(200)
            t.pencolor(100, 150, 200)
            t.setpos(i.x, i.y)
            t.pendown()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
"""