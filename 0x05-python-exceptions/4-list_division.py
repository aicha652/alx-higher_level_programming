#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        while i:
            list_length[i] = my_list_1[i] / my_list_2[i]
            i += 1
    except ZeroDivisionError:
        print("division by 0")
        list_length[i] = 0
    except Exception as e:
        if type(my_list_1[i]) and type(my_list_2[i]) is not int or float:
            print("wrong type")
            list_length[i] = 0
    except Exception as e:
        if len(my_list_1) != len(my_list_2):
            print("out of range")
            list_length[i] = 0
    finally:
        print("{}".format(list_length))
        return list(list_length)
