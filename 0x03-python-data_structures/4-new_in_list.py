#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = []
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        for i in my_list:
            copied_list.append(i)
        copied_list[idx] = element
        return (copied_list)
