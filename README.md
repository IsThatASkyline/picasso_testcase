# picasso_testcase

## Установка и запуск
~~~
git clone https://github.com/IsThatASkyline/picasso_testcase.git
cd picasso_testcase
docker compose up --build
~~~

## API

### Для просмотра загруженных файлов
~~~
http://127.0.0.1:8000/api/v1/uploader/files/
~~~

### Для загрузки файла
~~~
http://127.0.0.1:8000/api/v1/uploader/upload/
~~~
