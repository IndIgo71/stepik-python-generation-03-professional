from itertools import accumulate


def factorials(n):
    return accumulate(range(1, n + 1), lambda x, y: x * y)
