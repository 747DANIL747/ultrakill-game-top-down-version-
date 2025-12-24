# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-tk && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY src/ ./src/

# Создаем точку входа
CMD ["python", "./src/main.py"]

# Информация о контейнере
LABEL maintainer="student@university.edu"
LABEL version="1.0.0"
LABEL description="ULTRAKILL-like Game Course Project"