def simple_sequence():
    value = 1
    while True:
        for _ in range(value):
            yield value
        value += 1
