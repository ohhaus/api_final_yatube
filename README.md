# Yatube API

API для социальной сети Yatube. Позволяет пользователям создавать посты, комментировать их, подписываться на других авторов и управлять подписками.

## Возможности API

- Создание, редактирование, удаление и просмотр постов
- Создание, редактирование, удаление и просмотр комментариев к постам
- Просмотр сообществ
- Подписка и отписка от авторов
- Получение и обновление JWT-токена
- Просмотр и фильтрация подписок

## Технологии

- Python 3.9+
- Django 3.2.16
- Django REST framework 3.12.4
- Simple JWT
- SQLite3

## Как запустить проект

1. Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/ohhaus/api_final_yatube.git
cd api_final_yatube
```

2. Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
source venv/Scripts/activate  # для Windows
```

3. Установите зависимости из requirements.txt:
```
pip install -r requirements.txt
```

4. Выполните миграции:
```
cd yatube_api
python manage.py migrate
```

5. Запустите проект:
```
python manage.py runserver
```

## Примеры запросов к API

### Получение публикаций
```
GET /api/v1/posts/
```

### Создание публикации
```
POST /api/v1/posts/

{
    "text": "Текст публикации",
    "group": 1
}
```

### Получение комментариев
```
GET /api/v1/posts/{post_id}/comments/
```

### Создание комментария
```
POST /api/v1/posts/{post_id}/comments/

{
    "text": "Текст комментария"
}
```

### Получение JWT-токена
```
POST /api/v1/jwt/create/

{
    "username": "username",
    "password": "password"
}
```

## Документация

После запуска проекта документация доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Тестирование

Для запуска тестов используйте команду:
```
pytest
```

## Авторы

- ohhaus

## Лицензия

Этот проект лицензирован под MIT License
