import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    line_dicts = (dict(zip(headers, data)) for data in reader)
    print(sum(int(line['raisedAmt']) for line in line_dicts if line['round'] == 'a'))
