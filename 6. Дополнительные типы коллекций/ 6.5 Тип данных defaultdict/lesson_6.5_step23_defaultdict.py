from collections import defaultdict


def flip_dict(dict_of_lists):
    d = defaultdict(list)
    for key, value in dict_of_lists.items():
        for el in value:
            d[el].append(key)
    return d
