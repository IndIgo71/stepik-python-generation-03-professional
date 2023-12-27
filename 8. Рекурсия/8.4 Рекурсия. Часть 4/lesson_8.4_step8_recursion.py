def dict_travel(nested_dicts, path=''):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel(v, f'{path}{k}.')
        else:
            print(f'{path}{k}: {v}')
