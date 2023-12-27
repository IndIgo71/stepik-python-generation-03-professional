def convert(string):
    upper_count, lower_count = 0, 0
    for c in string:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1

    return string.upper() if upper_count > lower_count else string.lower()
