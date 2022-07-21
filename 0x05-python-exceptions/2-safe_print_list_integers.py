#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0

        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            n += 1
    except (ValueError, TypeError):
        pass
    finally:
        print()
        return n
