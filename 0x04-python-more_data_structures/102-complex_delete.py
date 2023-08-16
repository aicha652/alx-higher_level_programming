#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_delete.append(k)
    for key_del in keys_delete:
        del a_dictionary[key_del]
    return a_dictionary
