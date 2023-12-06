#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list = set(list(my_list))

    for i in my_list:
        sum += i
    return (sum)
