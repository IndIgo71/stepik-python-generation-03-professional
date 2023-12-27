from collections import Counter
import csv

with open('name_log.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    email_changes = Counter(row['email'] for row in reader)
    for email, count in sorted(email_changes.items()):
        print(f'{email}: {count}')
