def safe_function(fct, *args):
    import sys
    try:
        r = fct(args[0], args[1])
    except Exception as e:
        print("Exception: ", e, file=sys.stderr)
        return None
    return r
