def filter_anagrams(word, words):
    return list(filter(lambda w: sorted(w) == sorted(word), words))
