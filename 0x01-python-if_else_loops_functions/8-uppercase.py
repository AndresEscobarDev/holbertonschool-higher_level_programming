#!/usr/bin/python3
def uppercase(s):
    l = ""
    for i in range(0, len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            l = ord(s[i]) - 32
        else:
            l = ord(s[i])
        if i + 1 < len(s):
            print("{:c}".format(l), end="")
        else:
            print("{:c}".format(l))
