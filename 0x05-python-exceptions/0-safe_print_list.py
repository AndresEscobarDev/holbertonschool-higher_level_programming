def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            i += 1
        except:
            print()
            return i
    print()
    return i