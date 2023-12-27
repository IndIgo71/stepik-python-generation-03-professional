from collections import Counter
import csv, json

with (open('quarter1.csv', 'r', encoding='utf-8') as fq1,
      open('quarter2.csv', 'r', encoding='utf-8') as fq2,
      open('quarter3.csv', 'r', encoding='utf-8') as fq3,
      open('quarter4.csv', 'r', encoding='utf-8') as fq4,
      open('prices.json', 'r', encoding='utf-8') as fp):
    _, *q1 = csv.reader(fq1, delimiter=',')
    _, *q2 = csv.reader(fq2, delimiter=',')
    _, *q3 = csv.reader(fq3, delimiter=',')
    _, *q4 = csv.reader(fq4, delimiter=',')
    prices = json.load(fp)

    res = Counter()
    for q in [q1, q2, q3, q4]:
        for sale in q:
            res += Counter({sale[0]: sum(map(int, sale[1:]))})

    res = Counter({product: prices[product] * res[product] for product in res})

    print(res.total())
