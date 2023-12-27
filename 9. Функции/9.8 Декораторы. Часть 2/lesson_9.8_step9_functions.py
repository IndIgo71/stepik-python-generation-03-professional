from functools import wraps


def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return wrapper
