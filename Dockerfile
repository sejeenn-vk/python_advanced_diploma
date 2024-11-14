# Используем базовый образ Python
FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-dev supervisor \
    nginx && rm -rf /var/lib/apt/lists/*

# Установка приложения и его зависимостей
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения внутрь контейнера
COPY main.py /src/
COPY static /src/static/
COPY nginx.conf /etc/nginx/nginx.conf
COPY
# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]