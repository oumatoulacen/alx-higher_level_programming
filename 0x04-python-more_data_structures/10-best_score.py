#!/usr/bin/python3

def best_score(a_dictionary):
    score = 0
    key = None
    if a_dictionary is None:
        return key
    for k, v in a_dictionary.items():
        if score < v:
            score = v
            key = k
    return key
