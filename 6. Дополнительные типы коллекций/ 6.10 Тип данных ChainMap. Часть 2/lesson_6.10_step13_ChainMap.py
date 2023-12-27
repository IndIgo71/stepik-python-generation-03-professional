from collections import ChainMap


def get_all_values(chainmap, key):
    res = set()
    for d in chainmap.maps:
        if key in d:
            res.add(d[key])

    return res
