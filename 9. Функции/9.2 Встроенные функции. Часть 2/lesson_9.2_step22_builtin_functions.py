f = input()
a, b = map(int, input().split())
results = [eval(f) for x in range(a, b + 1)]

print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(results)}')
print(f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(results)}')
