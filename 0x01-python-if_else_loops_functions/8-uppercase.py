#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            s = str[i]
            s = ord(s)
            s = s - 32
            s = chr(s)
            str = str[:i] + s + str[i+1:]
    print(str)
    return None
