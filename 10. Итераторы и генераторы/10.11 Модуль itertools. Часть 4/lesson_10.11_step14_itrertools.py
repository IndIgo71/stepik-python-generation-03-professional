from itertools import groupby


def group_anagrams(words):
    return [tuple(val) for _, val in groupby(sorted(words, key=sorted), key=sorted)]


groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)
