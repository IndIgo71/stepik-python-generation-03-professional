from collections import Counter

words = Counter(map(str.lower, input().split()))
print(max(words.items(), key=lambda x: (x[1], x[0]))[0])
