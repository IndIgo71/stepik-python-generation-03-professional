from zipfile import ZipFile


def extract_this(zipe_name: str, *args):
    with ZipFile(zipe_name, 'r') as zip_file:
        if len(args) == 0:
            zip_file.extractall()
        else:
            zip_file.extractall(members=args)
