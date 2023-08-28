#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for elem in my_list:
            if i < x:
                print('{}'.format(elem), end="")
                i += 1
        print()
        return i
    except Exception as err:
        print("error", err)
        return i
