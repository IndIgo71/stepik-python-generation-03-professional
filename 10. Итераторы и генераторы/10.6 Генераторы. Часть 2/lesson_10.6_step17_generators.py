from functools import reduce


def count_iterable(iterable):
    return reduce(lambda x, y: x + 1, iterable, 0)
