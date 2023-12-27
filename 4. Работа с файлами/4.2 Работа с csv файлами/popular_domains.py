import csv

with open('data.csv', mode='r', encoding='utf-8') as file_data, open('domain_usage.csv', mode='w', encoding='utf-8',
                                                                     newline='') as file_out:
    data = csv.DictReader(file_data, delimiter=',')

    out_data = dict()
    for item in data:
        domain = item['email'].split('@')[1]
        out_data[domain] = out_data.get(domain, 0) + 1

    writer = csv.writer(file_out, delimiter=',')
    writer.writerow(['domain', 'count'])
    writer.writerows(sorted(out_data.items(), key=lambda x: (x[1], x[0])))
