from functools import wraps


def takes(*dargs):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not all(map(lambda x: isinstance(x, dargs), [*args] + [*kwargs.values()])):
                raise TypeError
            return function(*args, **kwargs)

        return wrapper

    return decorator

