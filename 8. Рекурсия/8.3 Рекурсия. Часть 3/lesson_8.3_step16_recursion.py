def to_binary(number):
    if number == 0:
        return 0
    else:
        return number % 2 + 10 * to_binary(number // 2)
