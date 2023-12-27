from collections import defaultdict


def wins(pairs):
    d = defaultdict(set)
    for winner, loser in pairs:
        d[winner].add(loser)

    return d
