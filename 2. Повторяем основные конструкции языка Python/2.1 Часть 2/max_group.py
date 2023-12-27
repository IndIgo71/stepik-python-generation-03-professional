def max_group(n):
    lst = list(range(1, n + 1))
    d = {s: [n for n in lst if sum(map(int, str(n))) == s] for s in set(sum(map(int, str(n))) for n in lst)}
    return max(map(len, d.values()))


n = int(input())
print(max_group(n))
