import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    content = json.load(file)
    district = {}
    operating_company = {}
    for row in content:
        district[row['District']] = district.get(row['District'], 0) + 1
        if row['OperatingCompany']:
            operating_company[row['OperatingCompany']] = operating_company.get(row['OperatingCompany'], 0) + 1

    largest_district = tuple(filter(lambda x: x[1] == max(district.values()), district.items()))[0]
    largest_operating_company = \
    tuple(filter(lambda x: x[1] == max(operating_company.values()), operating_company.items()))[0]

    print(f"{largest_district[0]}: {largest_district[1]}")
    print(f"{largest_operating_company[0]}: {largest_operating_company[1]}")
