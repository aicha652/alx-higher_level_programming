#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary = dict(a_dictionary)
    a_dictionary.update((key, value * 2)
                        for key, value in a_dictionary.items())
    return a_dictionary
