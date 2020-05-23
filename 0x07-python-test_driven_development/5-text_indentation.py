#!/usr/bin/python3
"""Module Text-Indentation"""


def text_indentation(text):
    """  function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    new = ""
    j = 0
    while i < len(text) and text[i] == ' ':
        i +=1
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new += text[i]
            i += 1
            new += "\n\n"
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            new += text[i]
            i += 1
    for i in range(len(new)-1, 0, -1):
        if new[i] != ' ':
            break
        j += 1
    print(new[:len(new) - j], end="")
