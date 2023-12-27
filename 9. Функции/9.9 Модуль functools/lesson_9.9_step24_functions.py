from functools import lru_cache
import sys


@lru_cache()
def word_sort(word):
    return ''.join(sorted(word))


for word in sys.stdin.readlines():
    print(word_sort(word.strip()))
