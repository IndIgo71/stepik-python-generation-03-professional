from itertools import pairwise, starmap


def max_pair(iterable):
    return max(starmap(lambda a, b: a + b, pairwise(iterable)))
