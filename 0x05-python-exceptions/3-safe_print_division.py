def safe_print_division(a, b):
    try:
        r = a / b
    except:
        r = None
        return None
    finally:
        print("Inside result: {}".format(r))
    return r
