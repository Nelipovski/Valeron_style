# Docker Compose

Аргумент `restart` имеет атрибут
1. `no` - никогда ( по умолчанию )
1. `on-failure` - после критического сбоя
1. `always` - всегда

# Docker
## Dockerfile
- `FROM python:3.12`
  - `FROM` - инструкция 
  - ``python:``- имя базового образа 
  - `3.12`- версия базового образа
- `WORKDIR /app` - создание рабочей дериктории внутри образа
- `COPY . .` - копируем из текущей папки в папку `/app`
- `CMD ['python', 'main.py']`- выполнение команд
## Использование готовых образов (images)

- docker version - отображение версии докера

- Список контейнеров:
    - `docker ps` - список всех активных контейнеров
    - `docker ps -a` - список всех контейнеров (запущенных и остановленных)
    - `docker ps -a -q` - список всех контейнеров(только id)

- `docker images` - список всех образов

- `docker build` - запуск процесса создания образа
  - `-t` tag_name - название контейнера.

- Запуск контейнера:
    - `docker run -it` busybox - запуск контейнера busybox и вход в его терминал (`-it` interactive terminal)
    - `docker run -d` nginx - запуск nginx в фоновом режиме (`-d` detached - обособленный/отдельный)
    - `docker run --name test -d hello-world` - запуск контейнера фоном с именем 'test'
    - `docker run --name test -d --rm hello-world` - запуск контейнера фоном с удалением контейнера после выполнения

- Запуск длинных комманд в несколько строк:
```    
    docker run \
    --rm \ 
    -p 8181:80 \
    -d \
    nginx
```    

- Маршрутизация портов:
    - docker run -p 8080:80 nginx - запуск контейнера с проброской портов (-p) 8080 - внешний порт, 80 - порт внутри контейнера. Теперь веб интерфейс nginx доступен с локального пк по адресу http://localhost:8080/. Внешний порт : внутренний порт.

- Маршрутизация томов(папок):
    - docker run -v ${PWD}:/usr/share/hginx/html nginx - запуск контейнера с подключением (-v volume - том/папка) текущей директории терминала (${PWD}) в качестве тома для внутренней папки контейнера (/usr/share/hginx/html). Т.е. все данныхе из текущей папки будут доступны изнутри запущенного контейнера. Внешняя папка : внутренняя папка.
    - docker run --rm -d --name todos -p 8181:8000 -v ${PWD}:/usr/src/app/database/ todos-server

- Информация о контейнере:
    - docker container inspect 815350f185b7 - отображение ВСЕЙ информации о запущенном контейнере (по id)
    - docker container inspect 815350f185b7 | grep IPAddress - отображение ip адреса контейнера (по id)

- docker exec -it container-name sh - подключение к терминалу внутри контейнера

- Остановка контейнера:
    - docker stop 815350f185b7 - остановка контейнера по id
    - docker stop container_name - остановка контейнера по имени
    - docker kill 815350f185b7 - "принудительная" остановка контейнера по id

- Удаление:
    - docker rm name - удалить контейнер 'name' (либо можно передать id)
    - docker container prune - удалить все остановленные контейнеры

- docker system df - сколько места занимает docker


# Docker Images (Создание образа)

Этапы создания образа:

1. Создать dockerfile
2. Разместить этот файл в *корне* папки приложения
3. Dockerfile содержит инструкции по созданию образа
4. При создании образа можно указать имя и тег для образа
5. На основании готового образа можно создавать контейнеры
---

# SQL SHELL (psql)

`\l` - какие базы существуют.

`\c` - подключение к базе данных.

`\d` - таблицы

`\conninfo` - данные подключения к базе данных.

`CREATE TABLE name` - создание табллицы.

`DROP DATABASE name` - удаление базы данных.

`INSERT INTO name` - добовление данных в таблицу. 

```
Пример:

INSERT INTO имя таблицы (
    first_name,
    last name,
    gender,
    email,
    date_of_birth
)
VALUES('Valery', 'Zelenkevich', 'MALE', 'Neybeika@mail.ru', '1991-01-07');
```
-----
---
```
.venv
python3 -m venv .venv
source .venv/bin/activate

pip freeze - список пакетов
pip freeze > requirements.txt
pip install -r requirements.txt
```
```
# VS Code shortcuts

- `CMD + B` - show/hide sidebar
- `CMD + K + Z` - zen mode
- `CMD + P` - open file
- `SHIFT + F12` - show where function used
- `CMD + OPT + arrow left/right` - switch between tabs
- `CMD + W` - close tab
- `CMD + SHIFT + V` - preview file (.md)
- `CMD + K + V` - side preview file (.md)
- `F2` - change name for variable (everywhere)
- `OPT + SHIFT + arrow up/down` - copy line up and down
- `CTRL + SHIFT + U/L` - convert selected to UPPERCASE/lowercas
```