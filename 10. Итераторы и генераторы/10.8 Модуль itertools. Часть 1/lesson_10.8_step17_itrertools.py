from string import ascii_uppercase
from itertools import cycle


def alnum_sequence():
    return cycle(item for pair in zip(range(1, 27), ascii_uppercase) for item in pair)
