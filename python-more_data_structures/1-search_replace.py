#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    t = search
    for i in my_list:
        if i == search:
            new_list.append(replace)
        elif i != search and i != replace:
            new_list.append(i)
        elif i == replace:
            new_list.append(t)
    return new_list
