def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return 1
    except ValueError:
        return 0
