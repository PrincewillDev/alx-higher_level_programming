#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = sorted(a_dictionary)
    myValue = []
    for k in myKeys:
        myValue.append(a_dictionary[k])
    a_dictionary = dict(zip(myKeys, myValue))
    for k, v in a_dictionary.items():
        print("{}: {}".format(k, v))
