from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {repr(args)}, {repr(kwargs)}')
        result = func(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(result)}')
        return result

    return wrapper
