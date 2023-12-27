from functools import wraps


def add_attrs(**dkwargs):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        for k, v in dkwargs.items():
            setattr(wrapper, k, v)
        return wrapper

    return decorator
