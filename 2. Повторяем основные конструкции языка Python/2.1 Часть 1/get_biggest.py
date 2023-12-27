def get_biggest(numbers):
    if not numbers:
        return -1
    return int(''.join(sorted(map(str, numbers), key=lambda x: x * len(max(map(str, numbers), key=len)), reverse=True)))
