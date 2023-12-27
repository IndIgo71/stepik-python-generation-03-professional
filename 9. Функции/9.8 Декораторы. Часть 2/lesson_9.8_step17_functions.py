from functools import wraps


def prefix(string, to_the_end=False):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if to_the_end:
                result += string
            else:
                result = string + result
            return result

        return wrapper

    return decorator
