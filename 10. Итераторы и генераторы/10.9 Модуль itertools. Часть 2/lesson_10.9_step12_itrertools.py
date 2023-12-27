from itertools import dropwhile


def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)
