def same_parity(numbers):
    return list(filter(lambda n: numbers[0] % 2 == n % 2, numbers))
