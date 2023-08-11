#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    if args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif sys.argv[2] != '+' and '-' and '*' and '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    elif sys.argv[2] == '+':
        result = int(sys.argv[1]) + int(sys.argv[3])
        print('{} + {} = {}'.format(sys.argv[1], sys.argv[3], result))
    elif sys.argv[2] == '-':
        result = int(sys.argv[1]) - int(sys.argv[3])
        print('{} - {} = {}'.format(sys.argv[1], sys.argv[3], result))
    elif sys.argv[2] == '*':
        result = int(sys.argv[1]) - int(sys.argv[3])
        print('{} * {} = {}'.format(sys.argv[1], sys.argv[3], result))
    elif sys.argv[2] == '/':
        result = int(sys.argv[1]) - int(sys.argv[3])
        print('{} / {} = {}'.format(sys.argv[1], sys.argv[3], result))
