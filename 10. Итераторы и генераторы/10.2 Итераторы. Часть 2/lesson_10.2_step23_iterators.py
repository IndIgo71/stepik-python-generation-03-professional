def starmap(func, iterable):
    return map(func, *zip(*iterable))
