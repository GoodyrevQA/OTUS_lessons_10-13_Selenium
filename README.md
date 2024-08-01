# OTUS_lessons_10-13_Selenium
base Selenium

запуск Docker

инструкция: https://gist.github.com/konflic/ecd93a4bf7666d97d62bcecbe2713e55

коротко:
- docker-compose up -d - запустить сборку приложения
- docker ps - посмотреть запущенные контейнеры
- docker ps -a - посмотреть все контейнеры (включая потушенные)
- docker-compose down - потушить все контейнеры из docker-compose файла
- docker images - показать все сборки
- docker system prune -a - удалить все образы
- docker volume prune - очистить кеш

Для валидного пересбора контейнеров с обновлением конфигурации из файла, использовать команду docker-compose down -v если приложение запущено, или docker volume prune -a если приложение уже остановлено.

запуск:
0. включить Docker
1. в PowerShell командой gip узнать свой IPv4Address (например 192.168.0.17)  
2. в файле docker-compose.yaml установить переменной OPENCART_HOST значение своего ip и порт 8081 (OPENCART_HOST=192.168.0.17:8081)
3. в PowerShell перейти в папку, где лежит файл docker-compose.yaml
4. выполнить команду docker-compose up -d