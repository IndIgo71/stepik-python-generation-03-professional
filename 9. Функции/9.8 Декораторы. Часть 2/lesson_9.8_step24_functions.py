from functools import wraps


def ignore_exception(*exceptions):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')

        return wrapper

    return decorator
