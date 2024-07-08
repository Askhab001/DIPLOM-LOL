# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/

RUN pip install -r req.txt

# Копируем весь проект в контейнер
COPY ../../../Downloads /app/

# Выполняем миграции и собираем статические файлы
RUN python manage.py migrate

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
