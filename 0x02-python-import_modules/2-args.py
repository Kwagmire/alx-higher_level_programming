#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)

    if len == 2:
        argument = "argument"
    else:
        argument = "arguments"

    if len == 1:
        print("0 arguments.")
    else:
        print("{} {}:".format(len - 1, argument))

        for i in range(1, len):
            print("{}: {}".format(i, argv[i]))
