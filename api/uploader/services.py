import os

from core.models import File
from core.tasks import process_img, process_txt, process_docx, process_csv, process_any_other_extension


def get_file_extension(file):
    print(type(file))
    return os.path.splitext(str(file))[1]


def file_create(
    *,
    file: File
) -> File:
    file = File(file=file)
    file.full_clean()
    file.save()
    return file


def file_process(file_id: int, file_extension: str):
    # Match case
    if file_extension == '.png':
        print('Обработал png')
        process_img.delay(file_id)
    elif file_extension == '.txt':
        print('Обработал txt')
        process_txt.delay(file_id)
    elif file_extension == '.docx':
        print('Обработал docx')
        process_docx.delay(file_id)
    elif file_extension == '.csv':
        print('Обработал csv')
        process_csv.delay(file_id)
    else:
        print('Обработал файл')
        process_any_other_extension.delay(file_id)


def file_list():
    files = File.objects.all()
    return files
