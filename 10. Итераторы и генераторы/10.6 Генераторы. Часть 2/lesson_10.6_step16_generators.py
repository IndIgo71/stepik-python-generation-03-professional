def is_prime(number):
    if number == 1 or number % 2 == 0:
        return False
    return all(number % i != 0 for i in range(3, number, 2))
