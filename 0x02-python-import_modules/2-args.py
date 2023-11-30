#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argvLen = len(argv)
    if argvLen == 1:
        print("0 arguments.")
    elif argvLen == 2:
        print("{} argument:".format(argvLen - 1))
    else:
        print("{} arguments:".format(argvLen - 1))
    for index in range(1, len(argv)):
        print("{}:{}".format(index, argv[index]))
