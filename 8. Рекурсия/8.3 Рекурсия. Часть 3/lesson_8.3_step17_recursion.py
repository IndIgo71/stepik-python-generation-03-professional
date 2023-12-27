def minus_5_recursion(n) -> int:
    print(n)
    if n > 0:
        minus_5_recursion(n - 5)
        print(n)


minus_5_recursion(int(input()))
