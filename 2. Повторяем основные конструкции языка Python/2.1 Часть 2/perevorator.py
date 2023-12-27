def perevorator(n, x, y, a, b):
    lst = list(range(1, n + 1))
    lst[x - 1: y] = lst[x - 1: y][::-1]
    lst[a - 1: b] = lst[a - 1: b][::-1]
    return lst


n, x, y, a, b = map(int, input().split())
print(*perevorator(n, x, y, a, b))
