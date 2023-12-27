def get_all_values(nested_dicts, key):
    res = set()

    if key in nested_dicts:
        res.add(nested_dicts[key])

    for v in nested_dicts.values():
        if isinstance(v, dict):
            res.update(get_all_values(v, key))

    return res
