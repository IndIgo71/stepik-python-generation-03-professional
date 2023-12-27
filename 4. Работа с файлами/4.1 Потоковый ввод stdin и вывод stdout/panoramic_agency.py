import sys

lines = [line.strip() for line in sys.stdin]
theme = lines.pop()
news = {}
for line in lines:
    header, theme, reliability = line.split(' / ')
    news[theme] = news.setdefault(theme, []) + [(float(reliability), header)]

sys.stdout.writelines([item[1] + '\n' for item in sorted(news[theme], key=lambda x: x)])
