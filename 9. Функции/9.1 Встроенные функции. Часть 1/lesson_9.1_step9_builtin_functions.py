def non_negative_even(numbers):
    return all(map(lambda x: x >= 0 and x % 2 == 0, numbers))
