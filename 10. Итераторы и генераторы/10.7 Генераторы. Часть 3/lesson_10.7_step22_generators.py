def pairwise(iterable):
    iterator = iter(iterable)
    try:
        prev = next(iterator)
    except StopIteration:
        return

    for item in iterator:
        yield prev, item
        prev = item

    yield prev, None
