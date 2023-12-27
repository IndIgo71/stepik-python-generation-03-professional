def unique(iterable):
    yield from dict.fromkeys(iterable)
