from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    print(f"Объем исходных файлов: {sum(map(lambda x: x.file_size, info))} байт(а)")
    print(f"Объем сжатых файлов: {sum(map(lambda x: x.compress_size, info))} байт(а)")
