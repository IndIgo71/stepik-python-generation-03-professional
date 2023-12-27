from functools import wraps


def make_html(tag):
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator
