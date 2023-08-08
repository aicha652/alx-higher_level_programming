#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print('{}{}'.format(0, number) if number <= 9 else '{}'.format(number),
              end=', ')
    elif number == 99:
        print(number)
