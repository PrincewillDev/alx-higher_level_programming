#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None)
    else:
        newTuple = (len(sentence), sentence[0])
        return (newTuple)
