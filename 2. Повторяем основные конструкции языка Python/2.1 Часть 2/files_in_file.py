units = {'B': 2 ** 0, 'KB': 2 ** 10, 'MB': 2 ** 20, 'GB': 2 ** 30}

with open('files.txt', encoding='utf-8') as f:
    lines = f.read().splitlines()
    files_info = [line.split() for line in lines]
    data = {extension: sorted(filter(lambda file: extension == file[0].split('.')[1], files_info)) for extension in
            set(info[0].split('.')[1] for info in files_info)}
    for extension, files in sorted(data.items()):
        total = 0
        for file_name, file_size, unit in files:
            print(file_name)
            total += int(file_size) * units[unit]

        if units['KB'] <= total < units['MB']:
            total = round(total / units['KB'])
            unit = 'KB'
        elif units['MB'] <= total < units['GB']:
            total = round(total / units['MB'])
            unit = 'MB'
        elif total >= units['GB']:
            total = round(total / units['GB'])
            unit = 'GB'
        else:
            total = round(total)
            unit = 'b'

        print('-' * 10)
        print(f'Summary: {total} {unit}')
        print()


# импортируем тип date из модуля datetime
from datetime import date

# выводим текущую дату
print(date.today().isoweekday())