from zipfile import ZipFile


def convert_bytes(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1_000_000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / (1024 ** 2))} MB'
    else:
        return f'{round(size / (1024 ** 3))} GB'


with ZipFile('desktop.zip') as zip_file:
    files_info = zip_file.infolist()
    for file in files_info:
        path = list(filter(None, file.filename.split('/')))
        size = convert_bytes(file.file_size)
        if not file.is_dir():
            print(' ' * ((len(path) - 1) * 2) + f'{path[-1]} {size}')
        else:
            print(' ' * ((len(path) - 1) * 2) + f'{path[-1]}')
