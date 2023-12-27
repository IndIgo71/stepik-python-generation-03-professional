def recursive_sum(nested_lists):
    total = 0

    for i in nested_lists:
        if isinstance(i, list):
            total += recursive_sum(i)
        else:
            total += i

    return total
