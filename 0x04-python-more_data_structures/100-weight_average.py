#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    total_x = 0
    total_y = 0
    for x, y in my_list:
        total_x = total_x + (x * y)
        total_y = total_y + y
    aver = total_x / total_y
    return aver
