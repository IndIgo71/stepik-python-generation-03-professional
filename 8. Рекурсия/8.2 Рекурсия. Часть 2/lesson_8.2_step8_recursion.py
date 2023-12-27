def show_reversed():
    n = int(input())
    if n != 0:
        show_reversed()
    print(n)


show_reversed()
