from itertools import islice


def first_true(iterable, predicate):
    return next(islice(filter(predicate, iterable), 1), None)
