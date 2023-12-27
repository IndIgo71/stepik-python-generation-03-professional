from collections import Counter

words = Counter(map(len, input().split()))
for l, c in sorted(words.items(), key=lambda x: x[1]):
    print(f'Слов длины {l}: {c}')
