def get_min_max(iterable):
    itr = iter(iterable)
    try:
        min_item = max_item = next(itr)
    except StopIteration:
        return None

    for item in iterable:
        if item < min_item:
            min_item = item
        if item > max_item:
            max_item = item

    return min_item, max_item
