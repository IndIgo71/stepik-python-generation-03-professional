def polynom(x):
    res = x ** 2 + 1
    if not hasattr(polynom, 'values'):
        polynom.values = set()
    polynom.values.add(res)
    return res
