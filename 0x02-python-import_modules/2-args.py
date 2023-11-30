#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argvLen = len(argv)
    if argvLen == 1:
        print("0 arguments.")
    elif argvLen == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argvLen - 1))
    for index in range(1, len(argv)):
        print("{}: {}".format(index, argv[index]))
