from zipfile import ZipFile
from datetime import datetime

search_dt = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
with ZipFile('workbook.zip') as zip_file:
    infolist = zip_file.infolist()
    result = [file.filename.split('/')[-1] for file in infolist if
              not file.is_dir() and datetime(*file.date_time) > search_dt]
    print(*sorted(result), sep='\n')
