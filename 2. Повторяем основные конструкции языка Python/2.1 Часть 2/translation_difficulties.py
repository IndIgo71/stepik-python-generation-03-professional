from functools import reduce

n = int(input())
surveys = []
for _ in range(n):
    surveys.append(set(input().split(', ')))

result = reduce(lambda s1, s2: s1.intersection(s2), surveys)
if result:
    print('Сериал снять не удастся')
else:
    print(', '.join(sorted(result)))
