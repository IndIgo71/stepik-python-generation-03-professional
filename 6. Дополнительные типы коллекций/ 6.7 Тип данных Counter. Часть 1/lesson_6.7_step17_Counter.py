from collections import Counter

products = Counter(input().split(','))
for k, v in sorted(products.items()):
    print(f'{k}: {v}')
