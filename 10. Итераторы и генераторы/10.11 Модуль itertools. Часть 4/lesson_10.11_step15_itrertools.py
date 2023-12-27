from itertools import groupby, pairwise


def ranges(numbers):
    return [
        (min(tpl), max(tpl))
        for tpl in (
            tuple(vals)
            for _, vals in
            groupby(numbers, key=lambda x: numbers.index(x) - x)
        )
    ]
