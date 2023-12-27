import csv
from datetime import datetime

pattern = '%d/%m/%Y %H:%M'
with open('name_log.csv', mode='r', encoding='utf-8') as file, open('new_name_log.csv', mode='w', encoding='utf-8',
                                                                    newline='') as out_file:
    reader = csv.reader(file, delimiter=',')

    headers, *context = list(reader)
    context = sorted(context, key=lambda x: datetime.strptime(x[-1], pattern), reverse=True)
    d = dict()
    for row in context:
        d[row[1]] = d.setdefault(row[1], row)

    writer = csv.writer(out_file, delimiter=',')
    writer.writerow(headers)
    writer.writerows(sorted(d.values(), key=lambda x: x[1]))
