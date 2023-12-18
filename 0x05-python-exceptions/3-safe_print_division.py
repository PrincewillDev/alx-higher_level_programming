#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        if b == 0:
            raise(ZeroDivisionError)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
