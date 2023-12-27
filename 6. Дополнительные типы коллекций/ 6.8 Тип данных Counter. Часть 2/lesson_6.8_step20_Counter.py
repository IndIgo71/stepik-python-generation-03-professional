from collections import Counter


def print_bar_chart(data, mark):
    result = Counter(data)
    max_len = max(map(len, result))

    for key, cnt in sorted(result.items(), key=lambda x: -x[1]):
        print(f'{key.ljust(max_len)} |{mark * cnt}')
