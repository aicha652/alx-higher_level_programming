#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []

    while len(tuple_a) < 2:
        tuple_a += (0,)

    while len(tuple_b) < 2:
        tuple_b += (0,)

    for i in range(0, 2):
        new_tuple.append(tuple_a[i] + tuple_b[i])
    return tuple(new_tuple)
