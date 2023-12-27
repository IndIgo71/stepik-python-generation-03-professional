from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    files_info = [file for file in zip_file.infolist() if not file.is_dir()]
    print(*[f'''{file.filename.split('/')[-1]}
  Дата модификации файла: {datetime.strftime(datetime(*file.date_time), '%Y-%m-%d %H:%M:%S')}
  Объем исходного файла: {file.file_size} байт(а)
  Объем сжатого файла: {file.compress_size} байт(а)''' for file in
            sorted(files_info, key=lambda x: x.filename.split('/')[-1])],
          sep='\n\n')
