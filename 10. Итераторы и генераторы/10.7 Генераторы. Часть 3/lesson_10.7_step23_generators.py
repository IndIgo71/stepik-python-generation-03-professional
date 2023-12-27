def around(iterable):
    iterator = iter(iterable)
    prev = None
    try:
        current = next(iterator)
    except StopIteration:
        return

    for item in iterator:
        yield prev, current, item
        prev, current = current, item

    yield prev, current, None
