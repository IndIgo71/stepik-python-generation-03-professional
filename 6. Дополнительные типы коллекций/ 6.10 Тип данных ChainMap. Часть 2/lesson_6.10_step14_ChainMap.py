from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in chainmap.keys():
        for d in chainmap.maps:
            if key in d:
                d[key] = value
    else:
        chainmap.maps[0][key] = value
