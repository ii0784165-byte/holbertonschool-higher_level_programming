#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        if set_2.count(i) != 0:
            new_list.append(i)
    new_list.sort()
    return new_list
