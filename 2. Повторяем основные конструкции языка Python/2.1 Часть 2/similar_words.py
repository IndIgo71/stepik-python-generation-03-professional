def get_pattern(word, letters='ауоыиэяюёе'):
    return [idx for idx, letter in enumerate(word) if letter in letters]


search_word = input()
checking_words = [input() for _ in range(int(input()))]
pattern = get_pattern(search_word)

for word in checking_words:
    if get_pattern(word) == pattern:
        print(word)
