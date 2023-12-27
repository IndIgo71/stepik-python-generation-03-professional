from collections import Counter


def count_occurences(word: str, words: str):
    word_counts = Counter(words.lower().split())
    return word_counts[word.lower()]
