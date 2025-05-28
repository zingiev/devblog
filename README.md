# DevBlog

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2.21-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Статус](https://img.shields.io/badge/статус-%20закончен-green.svg)]()

DevBlog - это блог-платформа, разработанная на Django, которая позволяет создавать и публиковать статьи с поддержкой форматированного текста, изображений и тегов.

## Особенности

- Создание и редактирование статей с богатым текстовым редактором (CKEditor)
- Поддержка загрузки изображений
- Система тегов для категоризации статей
- Административная панель для управления контентом
- Адаптивный дизайн

## Технический стек

- Python 3.x
- Django 4.2.21
- Pillow 11.2.1 (для работы с изображениями)
- django-ckeditor 6.7.0 (для форматированного текста)
- django-taggit 5.0.1 (для системы тегов)
- gunicorn 23.0.0 (для production-сервера)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone [URL репозитория]
cd devblog
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

После этого сайт будет доступен по адресу http://127.0.0.1:8000/

## Структура проекта

- `blog/` - основное приложение блога
- `devblog/` - настройки проекта Django
- `manage.py` - скрипт управления Django
- `requirements.txt` - зависимости проекта
- `db.sqlite3` - база данных (в production рекомендуется использовать PostgreSQL)

## Лицензия

Проект распространяется под лицензией MIT. Подробности в файле LICENSE.
