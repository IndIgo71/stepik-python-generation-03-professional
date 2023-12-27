from collections import Counter

words = Counter(map(str.lower, input().split()))
print(words.most_common(1)[0][0])
