def stop_on(iterable, obj):
    iterator = iter(iterable)
    return iter(lambda: next(iterator), obj)
