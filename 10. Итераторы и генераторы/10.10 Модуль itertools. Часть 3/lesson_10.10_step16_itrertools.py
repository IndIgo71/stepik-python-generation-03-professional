from itertools import repeat, chain


def ncycles(iterable, n):
    return chain.from_iterable(repeat(tuple(iterable), n))
