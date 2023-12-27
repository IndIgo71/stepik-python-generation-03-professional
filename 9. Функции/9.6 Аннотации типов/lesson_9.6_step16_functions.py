from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    d = deque(numbers)
    d.rotate(step)
    numbers[:] = d
