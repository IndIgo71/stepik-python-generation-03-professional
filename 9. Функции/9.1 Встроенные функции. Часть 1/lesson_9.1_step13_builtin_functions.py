def my_pow(number):
    return sum(int(n) ** (i + 1) for i, n in enumerate(str(number)))
