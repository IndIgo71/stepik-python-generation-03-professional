def linear(nested_lists):
    res = []
    for el in nested_lists:
        if isinstance(el, list):
            res.extend(linear(el))
        else:
            res.append(el)
    return res
