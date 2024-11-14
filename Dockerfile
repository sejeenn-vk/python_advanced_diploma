# Используем базовый образ Python
FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-dev supervisor \
    nginx && rm -rf /var/lib/apt/lists/*

# Установка приложения и его зависимостей
COPY requirements.txt /src/
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Копируем исходный код приложения внутрь контейнера
COPY src /src/
COPY static /src/static/
COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini

WORKDIR /src


# Команда для запуска приложения
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/superviord.ini"]