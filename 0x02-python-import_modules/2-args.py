#!/usr/bin/python3
import sys

args = len(sys.argv) - 1


def main():
    if args == 0:
        print('{} arguments.'.format(args))
    elif args == 1:
        print('{} argument:'.format(args))
        print('{}: {}'.format(args, str(sys.argv[1])))
    else:
        index = 1
        print('{} arguments:'.format(args))
        while (args >= index):
            print('{}: {}'.format(index, str(sys.argv[index])))
            index = index + 1


if __name__ == "__main__":
    main()
