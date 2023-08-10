#!/usr/bin/python3
import sys

args = len(sys.argv) - 1


def main():
    if args == 0:
        print('0')
    else:
        index = 1
        sum = 0
        while(args >= index):
            sum = sum + int(sys.argv[index])
            index = index + 1
        print(sum)


if __name__ == "__main__":
    main()
