#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        first = sentence[0]
        length = len(sentence)
        return length, first
    else:
        first = None
        length = 0
        return length, first
