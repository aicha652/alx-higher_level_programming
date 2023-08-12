#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple=[]
    if len(tuple_a) == len(tuple_b):
        for i in range (0, len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])
        result = tuple(new_tuple)
        return (str(result))
    elif len(tuple_a) > 2 and len(tuple_b) == 2:
        for i in range (0, len(tuple_b)):
            new_tuple.append(tuple_a[i] + tuple_b[i])
        result = tuple(new_tuple)
        return (str(result))
    elif len(tuple_b) > 2 and  len(tuple_a) == 2:
        for i in range (0, len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])
        result = tuple(new_tuple)
        return (str(result))
    elif len(tuple_a) < 2 and len(tuple_b) == 2:
        for i in range (0, len(tuple_b)):
            if tuple_a[i] != None:
                new_tuple.append(tuple_a[i] + tuple_b[i])
            else:
                tuple_a[i] == 0
                new_tuple.append(tuple_a[i] + tuple_b[i])
    elif len(tuple_b) < 2 and len(tuple_a) == 2:
        for i in range (0, len(tuple_a)):
            if tuple_b[i] != None:
                new_tuple.append(tuple_a[i] + tuple_b[i])
            else:
                tuple_b[i] == 0
                new_tuple.append(tuple_a[i] + tuple_b[i])
