#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    if args == 0:
        print('{}'.format(args))
    else:
        index = 1
        sum = 0
        while(args >= index):
            sum = sum + int(sys.argv[index])
            index = index + 1
        print('{}'.format(sum))
