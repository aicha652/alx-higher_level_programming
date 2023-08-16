#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    uniq_integers = set(my_list)
    add = 0
    for i in uniq_integers:
        uniq_list.append(i)
    for j in range(len(uniq_list)):
        add = add + uniq_list[j]
    return add
