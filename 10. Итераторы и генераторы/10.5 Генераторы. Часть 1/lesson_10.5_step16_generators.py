def alternating_sequence(count=None):
    current = 0
    while current != count:
        current += 1
        yield (-current, current)[current % 2]
