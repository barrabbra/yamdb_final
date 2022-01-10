# api_yamdb
API музыкального проекта.

### Описание
Проект позволяет создавать, хранить и получать информацию о музыкальных произведениях.
Для получения прав создавать и комментирования записей необходимо пройти JWT-аутентификацию.
Получить информацию о произведениях могут все пользователи без исключений.
Более подробная информация доступна в документации по адресу /redoc/

### Статус проекта
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

### Технологии
Python 3.7
Django 3.0.5
djangorestframework 3.11.0
djangorestframework-simplejwt 4.6.0

### Запуск в  режиме разработчика
Склонируйте репозиторий на локальный компьютер выполнив в коммандной строке:
```
https://github.com/barrabbra/api_yamdb.git
```
Перейдите в репозиторий проекта;
Установите и активируйте виртуальное окружение:
```
python -m venv venv
. venv/bin/activate
```
Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
В корневой папке проекта (где располагается файл manage.py) выполните команду:
```
python3 manage.py runserver
```
Сервер будет доступен по адресу http://localhost:8000

### Правила заполнения env-файла
DB_ENGINE=django.db.backends.postgresql (движок базы данный, в данном случае PostgreSQL)
DB_NAME=название для базы данных
POSTGRES_USER=имя пользователя базы данных
POSTGRES_PASSWORD=пароль пользователя
DB_HOST=адрес БД
DB_PORT=порт БД
SECRET_KEY = секретный ключ django сервера

### Запуск проекта в контейнере
Перейдите в папку Infra;
Создайте env-файл и заполните согласно шаблона;
Выполните в коммандной строке:
```
docker-compose up
```
По окончании сборки откройте новый терминал, выполните миграции и соберите статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input 
```
Загрузите первоночальные данные в БД:
```
docker-compose exec web python manage.py loaddata fixtures.json
```

### Авторы
Бикеев Рустам
github: @barrabbra
Васильев Андрей
github: @coolspawn