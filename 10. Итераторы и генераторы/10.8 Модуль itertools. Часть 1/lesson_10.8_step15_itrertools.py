from itertools import count


def tabulate(func):
    yield from (func(i) for i in count(start=1))

