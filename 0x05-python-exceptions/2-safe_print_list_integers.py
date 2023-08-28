#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list:
        count += 1
    try:
        if x <= count:
            i = 0
            for elem in my_list:
                if i < x:
                    if type(elem) is int:
                        print("{:d}".format(elem), end="")
                        i += 1
            print()
            return i
    except Exception as e:
        print(f"{e}")
