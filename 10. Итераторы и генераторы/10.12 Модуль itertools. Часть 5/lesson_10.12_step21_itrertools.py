from itertools import product
from string import digits


def password_gen():
    yield from (''.join(i) for i in product(digits, repeat=3))
