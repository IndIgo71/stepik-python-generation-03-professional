def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def tribonacci_rec(n):
        res = cache.get(n)
        if not res:
            res = tribonacci_rec(n - 1) + tribonacci_rec(n - 2) + tribonacci_rec(n - 3)
            cache[n] = res
        return res

    return tribonacci_rec(n)
