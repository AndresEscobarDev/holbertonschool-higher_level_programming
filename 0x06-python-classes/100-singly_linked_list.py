#!/usr/bin/python3
"""Single linked list Module"""


class Node():
    """Sigly linked list Node.
    Private instance attribute: data:
        property def data(self):
        property setter def data(self, value):
    Private instance attribute: next_node:
        property def next_node(self).
        property setter def next_node(self, value).
    Instantiation with data and next_node.
    """
    def __init__(self, data, next_node=None):
        """Constructor"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Sigly linked list.
    Private instance attribute: head (no setter or getter).
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """
    def __init__(self):
        """Constructor"""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)
        """
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        if new.data < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        current = self.head
        while current.next_node and current.next_node.data < new.data:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        """Create the string for the print statement"""
        string = ""
        current = self.head
        while current:
            string += str(current.data)
            string += '\n'
            current = current.next_node
        return string[:-1]
