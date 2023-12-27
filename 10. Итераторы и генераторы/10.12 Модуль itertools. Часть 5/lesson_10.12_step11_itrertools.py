from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

total = 0
for r in range(1, len(wallet) + 1):
    for combo in set(combinations(wallet, r)):
        if sum(combo) == 100:
            total += 1
print(total)
