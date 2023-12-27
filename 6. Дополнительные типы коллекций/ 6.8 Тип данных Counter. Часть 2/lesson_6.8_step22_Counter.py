from collections import Counter

books = Counter(map(int, input().split()))
total = 0

for _ in range(int(input())):
    book, price = map(int, input().split())
    if book in books:
        total += price
        books -= Counter({book: 1})

print(total)
