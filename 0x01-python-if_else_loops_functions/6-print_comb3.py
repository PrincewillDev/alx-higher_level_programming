#!/usr/bin/python3
for num in range(1, 90):
    if num != 89:
        print("{:02d}".format(num), end=", ")
    else:
        print("{:02d}".format(num), end="\n")


