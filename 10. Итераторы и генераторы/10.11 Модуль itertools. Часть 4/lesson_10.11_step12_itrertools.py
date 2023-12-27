from itertools import groupby

text = input().split()

text.sort(key=lambda word: (len(word), word))
grp = groupby(text, key=lambda word: len(word))
for key, values in grp:
    print(f'{key} -> {", ".join(values)}')
