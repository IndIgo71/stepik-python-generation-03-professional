from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False):
    idx = 1 if by_values else 0
    for key, _ in sorted(ordered_dict.items(), key=lambda t: t[idx]):
        ordered_dict.move_to_end(key)
