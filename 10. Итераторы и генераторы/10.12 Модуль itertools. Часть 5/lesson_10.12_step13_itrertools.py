from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]
price = 100

total = 0
for r in range(1, int(price / min(wallet)) + 1):
    for combo in set(combinations_with_replacement(wallet, r)):
        if sum(combo) == price:
            total += 1
print(total)
