
FROM python:3.11.10-slim-bullseye
WORKDIR /app
COPY . /app

RUN pip install psycopg2-binary

RUN pip install --no-cache-dir -r requirements.txt || pip install --no-cache-dir psycopg2-binary pytest

# Команда для запуска тестов
CMD ["pytest", "test_db.py"]