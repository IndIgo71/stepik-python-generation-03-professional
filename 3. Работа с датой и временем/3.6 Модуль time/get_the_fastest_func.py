import time


def get_the_fastest_func(funcs, arg):
    result = {}
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        result[func] = end - start

    return min(result, key=lambda x: result[x])
