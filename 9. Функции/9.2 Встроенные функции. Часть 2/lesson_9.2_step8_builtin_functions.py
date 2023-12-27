def hash_as_key(objects):
    d = {}
    for obj in objects:
        d.setdefault(hash(obj), []).append(obj)
    d = {k: v[0] if len(v) == 1 else v for k, v in d.items()}

    return d
