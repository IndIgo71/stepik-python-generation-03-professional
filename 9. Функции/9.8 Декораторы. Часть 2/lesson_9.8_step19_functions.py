from functools import wraps


def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator
