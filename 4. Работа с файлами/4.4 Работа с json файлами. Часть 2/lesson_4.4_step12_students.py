import csv
import json

with (open(file='students.json', mode='r', encoding='utf-8') as infile,
      open(file='data.csv', mode='w', encoding='utf-8', newline='') as outfile):
    content = list(json.load(infile))
    headers = ['name', 'phone']
    students = sorted(
        [(row['name'], row['phone']) for row in content if int(row['age']) >= 18 and int(row['progress']) >= 75])

    writer = csv.writer(outfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(students)
