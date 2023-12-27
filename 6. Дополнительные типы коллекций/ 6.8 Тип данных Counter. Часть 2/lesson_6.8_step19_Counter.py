from collections import Counter


def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())
