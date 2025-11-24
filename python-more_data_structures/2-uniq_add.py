#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = []
    total = 0

    for n in my_list:
        if n not in unique_nums:
            unique_nums.append(n)
            total += n

    return total
