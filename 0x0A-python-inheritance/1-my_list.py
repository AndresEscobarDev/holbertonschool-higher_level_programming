#!/usr/bin/python3
""" MyList Module """


class MyList (list):
    """ MyList class.
    This class inherits from list """
    def print_sorted(self):
        """ Print the list in an orderly way """
        new = self[:]
        new.sort()
        print(new)
