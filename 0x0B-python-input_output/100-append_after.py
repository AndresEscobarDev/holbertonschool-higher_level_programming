#!/usr/bin/python3
""" AppendAfter Module """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        f.write(s)
