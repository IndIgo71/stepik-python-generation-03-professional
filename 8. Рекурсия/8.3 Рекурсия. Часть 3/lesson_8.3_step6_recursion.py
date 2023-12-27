def digit_count(num):
    if num == 0:
        return 0
    return 1 + digit_count(num // 10)


print(digit_count(int(input())))
