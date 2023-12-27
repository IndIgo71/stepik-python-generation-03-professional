import time


def calculate_it(func, *args):
    start = time.monotonic()
    res = func(*args)
    end = time.monotonic()
    return res, end - start
