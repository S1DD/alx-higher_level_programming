#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple containing the length of a sentence and the first character"""
    if sentence == "":
        (0, None)

    return (len(sentence), sentence[0])
