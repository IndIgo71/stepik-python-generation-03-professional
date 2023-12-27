def sand_clock(start, step):
    res = f"{str(start) * step:^16}"
    print(res)
    if start != 4:
        sand_clock(start + 1, step - 4)
        print(res)


sand_clock(1, 16)
