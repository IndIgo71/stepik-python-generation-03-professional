from collections import Counter

words = Counter(map(str.lower, input().split()))
min_cnt = words.most_common()[-1][1]
print(', '.join(sorted([item[0] for item in words.items() if item[1] == min_cnt])))
