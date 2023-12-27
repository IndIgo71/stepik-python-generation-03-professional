def get_pow(a, n):
    if n == 0 or a == 0:
        return 1
    return a * get_pow(a, n - 1)
