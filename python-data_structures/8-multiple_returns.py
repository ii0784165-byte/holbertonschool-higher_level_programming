#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    if len(sentence) == 0 :
        return None
    else:
        print("Length: {:d} - First character: {}".format(len(sentence),first))
