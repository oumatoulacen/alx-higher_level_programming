#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_diff = set(map(lambda x: x if x not in set_1 else None, set_2)) \
            | set(map(lambda x: x if x not in set_2 else None, set_1))
    only_diff.discard(None)
    return only_diff
