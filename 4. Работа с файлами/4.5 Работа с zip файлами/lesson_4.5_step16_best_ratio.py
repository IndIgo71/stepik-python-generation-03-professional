from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    infolist = zip_file.infolist()
    files = list(filter(lambda x: not x.is_dir(), infolist))
    best_ratio = min(map(lambda x: x.compress_size / x.file_size, files))
    filename = [x for x in files if x.compress_size / x.file_size == best_ratio][0].filename
    print(filename.split('/')[-1])
