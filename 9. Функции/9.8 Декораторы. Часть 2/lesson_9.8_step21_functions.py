from functools import wraps


def returns(datatype):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if not isinstance(result, datatype):
                raise TypeError

            return result

        return wrapper

    return decorator
