def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]

    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value:
                return value
