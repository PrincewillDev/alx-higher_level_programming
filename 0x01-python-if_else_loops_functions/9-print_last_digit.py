#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastDigit = number % 10
        print("{}".format(lastDigit), end="")
        return lastDigit
    else:
        lastDi = abs(number) % 10
        print("{}".format(lastDi), end="")
        return lastDi
    print()
