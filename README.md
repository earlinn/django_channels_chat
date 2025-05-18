# django_channels_chat

![Static Badge](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue) 
![Static Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=green)
![WebSockets](https://img.shields.io/badge/WebSockets-000000?logo=websocket&logoColor=white)
![Static Badge](https://img.shields.io/badge/redis-%23DC382D.svg?logo=redis&logoColor=white)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![code style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Описание проекта

Чат на вебсокетах, реализованный с использованием Django Channels. Он позволяет пользователям общаться в реальном времени в отдельных комнатах. Проект был создан на основе инструкции из статьи на Хабре: [https://habr.com/ru/companies/otus/articles/852510/](https://habr.com/ru/companies/otus/articles/852510/), с добавлением следующих улучшений:

- **Авторизация пользователей**: Только авторизованные пользователи могут входить в комнаты.
- **Отображение имени пользователя**: В чате отображается, какой пользователь отправил сообщение.

## Памятка по работе с Poetry

Управление зависимостями осуществляется с помощью Poetry.

- После клонирования репозитория разворачиваем в проекте Poetry командой `poetry init` (если в проекте еще нет файла pyproject.toml), в Compatible Python versions вписываем нужную версию питона, если предложенная не подходит,
например, так: Compatible Python versions [^3.10]:  ^3.12
- Чтобы виртуальное окружение хранилось в папке самого проекта, надо один раз выполнить команду
`poetry config virtualenvs.in-project true`, но если ее уже выполняли раньше для других проектов
на этом же компьютере, то заново ее выполнять не нужно
- Создание виртуального окружения: если системная версия питона соответствует нужной на проекте,
то команда `poetry env activate`, если не соответствует, то команда `poetry env use /usr/bin/python3.<вставить нужное>`, например, так: `poetry env use /usr/bin/python3.12`
- В папке проекта появится папка .venv, далее можно устанавливать зависимости командой `poetry add` и т.п.

Основные команды:
- Активировать виртуальное окружение: `eval $(poetry env activate)`
- Удалить текущее активированное виртуальное окружение: `poetry env remove`
- Установить зависимости проекта: `poetry install`
- Добавить зависимость: `poetry add <название зависимости>` (можно указать несколько через пробел)
- Добавить dev-зависимость: `poetry add <название зависимости> --dev` (или -D)
- Удалить зависимость: `poetry remove <название зависимости>` (можно с флагом -D для dev-зависимостей)

Дока:
- https://python-poetry.org/docs/

## Команды для работы проекта

См. команды в Makefile.
Можно их копировать и запускать из терминала вручную, а можно через make.
[Как установить make на Ubuntu](https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/)

Список доступных команд:

- **`make startapp`**: Создаёт новое приложение в папке `src`. Замените `<name>` на имя вашего приложения.
- **`make run`**: Запускает встроенный WSGI-сервер разработки Django.
- **`make uvicorn`**: Запускает сервер Uvicorn для работы с ASGI-приложением.
- **`make makemig`**: Создаёт миграции для изменений в моделях.
- **`make migrate`**: Применяет миграции к базе данных.
- **`make superuser`**: Создаёт суперпользователя с именем `admin` и email `test@test.com`.
- **`make superuser-empty`**: Создаёт суперпользователя с вводом данных вручную.
- **`make shell`**: Открывает Django shell.
- **`make collectstatic`**: Собирает статические файлы в папку, указанную в `STATIC_ROOT`.
- **`make redis-server`**: Запускает Redis-сервер в Docker-контейнере.
- **`make redis-server-start`**: Запускает уже созданный контейнер Redis.
- **`make redis-server-stop`**: Останавливает контейнер Redis.
- **`make redis-server-exec`**: Открывает консоль Redis внутри контейнера.

Для выполнения команды используйте:

```bash
make <команда>
```

Например, чтобы запустить сервер разработки Django, выполните:

```bash
make run
```

## Пример .env-файла в папке src/config
```
SECRET_KEY = <your key>
REDIS_HOST = localhost
REDIS_PORT = 6379
```
