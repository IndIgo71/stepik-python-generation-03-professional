from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    print(len(list(filter(lambda x: not x.is_dir(), zip_file.filelist))))
