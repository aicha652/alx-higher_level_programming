#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(i): 0 for i in 'Cc'})
    return new_string
