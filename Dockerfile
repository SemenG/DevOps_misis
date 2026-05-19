FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем нашу папку со всем кодом и файлом books.csv внутри
COPY app/ ./app/

EXPOSE 8000

# ИСПРАВЛЕНО: заменена точка на двоеточие перед app
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]