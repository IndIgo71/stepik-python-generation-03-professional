import re


def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    pattern = re.compile(r'^[A-Z][a-z]*$')
    if re.match(pattern, name) is None:
        raise ValueError('Имя не является корректным')

    return len(names) + 1
