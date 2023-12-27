def flatten(nested_list):
    for el in nested_list:
        if isinstance(el, list):
            yield from flatten(el)
        else:
            yield el
