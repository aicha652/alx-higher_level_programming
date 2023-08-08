#!/usr/bin/python3
numbers1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for number1 in numbers1:
    for number2 in numbers2:
        result = '{}{}'.format(number1, number2)
        if (result == '99'):
            print(result)
        else:
            print('{}{}, '.format(number1, number2), end='')
