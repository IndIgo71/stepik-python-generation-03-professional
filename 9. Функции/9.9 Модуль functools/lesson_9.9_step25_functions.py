from functools import lru_cache


@lru_cache()
def ways(n):
    if n > 1:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)
    return (1, 0)[n < 1]
