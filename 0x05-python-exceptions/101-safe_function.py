def safe_function(fct, *args):
    import sys
    try:
        r = fct(args[0], args[1])
        return r
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
