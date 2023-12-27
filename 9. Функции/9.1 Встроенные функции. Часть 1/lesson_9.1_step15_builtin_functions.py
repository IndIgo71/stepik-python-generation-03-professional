def zip_longest(*args, fill=None):
    longest = max(map(len, args))
    res = list(map(lambda x: x + ([fill] * (longest - len(x))), args))
    return list(zip(*res))
