def is_power(number):
    if number > 1:
        return is_power(number / 2)
    else:
        return number == 1
