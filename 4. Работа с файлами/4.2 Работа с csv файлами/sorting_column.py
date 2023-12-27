import csv

col_num = int(input()) - 1
with open('deniro.csv', mode='r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    print(*[','.join(row) for row in
            sorted(rows, key=lambda row: int(row[col_num]) if row[col_num].isdigit() else row[col_num])], sep='\n')
