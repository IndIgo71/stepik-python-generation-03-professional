def print_given(*args, **kwargs):
    for item in args:
        print(f'{item} {type(item)}')

    for k, v in sorted(kwargs.items()):
        print(f'{k} {v} {type(v)}')
