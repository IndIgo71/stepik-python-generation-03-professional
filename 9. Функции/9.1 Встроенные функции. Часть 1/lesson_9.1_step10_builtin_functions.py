def is_greater(lists, number):
    return any(map(lambda x: sum(x) > number, lists))
