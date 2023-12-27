def is_valid(string):
    return all(map(lambda c: c in '0123456789', string)) and 4 <= len(string) <= 6
