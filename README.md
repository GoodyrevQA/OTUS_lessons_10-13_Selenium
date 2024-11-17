# OTUS_lessons_10-20_Selenium

[![Header](https://github.com/GoodyrevQA/OTUS_auto_web_QA_2024/blob/main/assets/OTUS.jpg)](https://github.com/GoodyrevQA/OTUS_auto_web_QA_2024)

### Languages and Tools used:
[![Pycharm](https://img.shields.io/badge/-Pycharm-24292f??style=for-the-badge&logo=Pycharm&logoColor=79ae42)](https://github.com/GoodyrevQA)
[![Python](https://img.shields.io/badge/-Python-24292f??style=for-the-badge&logo=Python&logoColor=47c5fb)](https://github.com/GoodyrevQA/python_tg_bot)
[![Selenium](https://img.shields.io/badge/-Selenium-24292f??style=for-the-badge&logo=Selenium&logoColor=00bf0d)](https://github.com/GoodyrevQA/OTUS_lessons_10-20_Selenium)
[![pytest](https://img.shields.io/badge/-pytest-24292f??style=for-the-badge&logo=pytest&logoColor=0099d9)](https://github.com/GoodyrevQA/python_autotests)
[![Git](https://img.shields.io/badge/-Git-24292f??style=for-the-badge&logo=Git&logoColor=f43010)](https://github.com/GoodyrevQA)
[![Docker](https://img.shields.io/badge/-Docker-24292f??style=for-the-badge&logo=Docker&logoColor=47c5fb)](https://github.com/GoodyrevQA/OTUS_lessons_10-20_Selenium)


### Selenium

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



описание задания с docker compose https://github.com/OtusTeam/QA-Python/blob/master/docker-compose/hw.md
коротко:
- в docker-compose.yml описываются шаги создания и запуска прилложения opencart,
которое состоит из 3-х контейнеров: phpadmin, mariadb, opencart + создание и запуск
контейнера с тестами для него.
- для запуска используется selenoid, который должен быть поднят отдельно (в примере сеть также называется selenoid).
```
docker run -d --name selenoid-ui --network selenoid -p 8090:8080 aerokube/selenoid-ui:1.10.11 --selenoid-uri http://selenoid:4444
```
в в docker-compose.yml добавлен блок
```
networks:
  default:
    name: selenoid
    external: true
```
за счет этого 4 сервиса и сам selenoid будут находиться в одной сети, что обеспечит их связность и позволит им взаимодействовать между собой.
- Так как opencart не стартует мгновенно, при запуске сервиса с тестами нужно организовать ожидание,
пока opencart полностью перейдёт в рабочее состояние. Для этого можно использовать скрипт wait-for-it.sh.
- для сборки приложения и запуска тестов нужно предварительно поднять selenoid и выполнить команду 
```
docker compose up
```
