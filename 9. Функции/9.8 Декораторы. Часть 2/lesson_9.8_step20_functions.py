from functools import wraps


def strip_range(start, end, char='.'):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result[:start] + char * (min(end, len(result)) - start) + result[end:]

        return wrapper

    return decorator

