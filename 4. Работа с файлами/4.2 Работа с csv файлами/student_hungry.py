import csv

with open('prices.csv', mode='r', encoding="utf-8") as f:
    reader = list(csv.reader(f))
    header = "".join(reader[0]).split(";")
    cheap_products = []
    for line in reader[1:]:
        arr_prices = "".join(line).split(";")
        min_price = min(map(int, arr_prices[1:]))
        product = header[arr_prices.index(str(min_price))]
        cheap_products.append((min_price, product, arr_prices[0]))

    print(*min(cheap_products, key=lambda x: x[0])[1:], sep=": ")
