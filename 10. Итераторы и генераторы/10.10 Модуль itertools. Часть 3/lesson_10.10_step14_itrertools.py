from itertools import pairwise


def is_rising(iterable):
    return all(x < y for x, y in pairwise(iterable))
