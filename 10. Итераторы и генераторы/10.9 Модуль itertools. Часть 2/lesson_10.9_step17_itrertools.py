from itertools import dropwhile


def first_largest(iterable, number):
    return next(map(lambda x: x[0], dropwhile(lambda x: x[1] < number, enumerate(iterable))), -1)
