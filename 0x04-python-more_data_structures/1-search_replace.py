#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(my_list)
    new_list = my_list
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
