import csv

with open('salary_data.csv', mode='r', encoding='utf-8') as f:
    rows = csv.DictReader(f, delimiter=';')
    companies = {}
    for row in rows:
        companies.setdefault(row['company_name'], []).append(int(row['salary']))

    avg_sal_companies = {k: sum(v) / len(v) for k, v in companies.items()}
    print(*sorted(avg_sal_companies, key=lambda c: (avg_sal_companies[c], c)), sep='\n')
