def upper(func):
    def wrapper(*args, **kwargs):
        args = tuple(map(lambda x: x.upper() if isinstance(x, str) else x, args))
        kwargs = {k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


print = upper(print)

print('are you in trouble?')
