from core.models import File
from picasso_testcase.celery_app import app


@app.task
def process_img(file_id: int):
    file = File.objects.get(id=file_id)
    # Some process
    file.processed = True
    file.full_clean()
    file.save()


@app.task
def process_txt(file_id: int):
    file = File.objects.get(id=file_id)
    # Some process
    file.processed = True
    file.full_clean()
    file.save()


@app.task
def process_docx(file_id: int):
    file = File.objects.get(id=file_id)
    # Some process
    file.processed = True
    file.full_clean()
    file.save()


@app.task
def process_csv(file_id: int):
    file = File.objects.get(id=file_id)
    # Some process
    file.processed = True
    file.full_clean()
    file.save()


@app.task
def process_any_other_extension(file_id: int):
    file = File.objects.get(id=file_id)
    # Some process
    print(type(File))
    print('Я тут')
    file.processed = True
    file.full_clean()
    file.save()
