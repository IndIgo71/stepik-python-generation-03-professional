from itertools import zip_longest, repeat


def grouper(iterable, n):
    it = iter(iterable)
    return zip_longest(*repeat(it, n))
