# Устанавка базового образ
FROM python:3.12-alpine

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN apk add --no-cache coreutils
RUN chmod +x wait-for-it.sh

# Копирование остальных файлов проекта
COPY . .

# Запуск 
# CMD ["pytest", "--remote", "--url", "http://192.168.0.24:8081", "--executor", "192.168.0.24"]
CMD ["sh"]

# docker run --network selenoid opencart-tests-sh pytest --remote --url http://192.168.0.24:8081 --executor 192.168.0.24