#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
       return (None, None)
    else:
        tup = (a, sentence[0])
        return tup
