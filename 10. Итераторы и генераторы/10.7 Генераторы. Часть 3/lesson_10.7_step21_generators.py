def with_previous(iterable):
    prev = None
    for item in iterable:
        yield item, prev
        prev = item
