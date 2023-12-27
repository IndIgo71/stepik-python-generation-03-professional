from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    tmp = chainmap.copy()
    if not from_left:
        tmp.maps.reverse()
    return tmp.get(key)
