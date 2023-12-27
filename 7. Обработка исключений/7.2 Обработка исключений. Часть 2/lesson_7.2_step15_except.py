import sys

words_count = 0
nums_sum = 0
for word in sys.stdin.readlines():
    try:
        nums_sum += int(word)
    except ValueError:
        try:
            nums_sum += float(word)
        except ValueError:
            words_count += 1
    except ValueError:
        words_count += 1

print(nums_sum, words_count, sep='\n')
