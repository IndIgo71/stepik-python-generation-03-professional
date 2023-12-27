from collections import Counter

words = Counter(input().split(','))
longest = max(map(len, words))
for word, count in sorted(words.items()):
    price = sum(map(lambda c: ord(c) if c.isalpha() else 0, word))
    print(f'{word.ljust(longest)}: {price} UC x {count} = {price * count} UC')
