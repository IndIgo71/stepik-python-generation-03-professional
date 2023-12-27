from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return function(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException

        return wrapper

    return decorator
