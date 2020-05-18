#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    l = []
    while i < list_length:
        try:
            r = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            r = 0
            print("wrong type")
        except IndexError:
            r = 0
            print("out of range")
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        finally:
            i += 1
            l.append(r)
    return l
