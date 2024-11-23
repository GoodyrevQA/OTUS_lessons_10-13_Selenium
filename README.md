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


### Настройка Jenkins:
Инструкция:
https://docs.google.com/document/d/1VsRfM31dv6cdzzRRVdK5Fiu_HEq0mcBmo2lu_PGVw3Y/edit?tab=t.0#heading=h.icoyi4idm65z

Находясь в директории с Dockerfile для создания образа Jenkins c доккером внутри 'docker-file-for-jenkins'
создать образ:
```
docker build -t jenkins-with-docker .
```

на основе образа создать контейнер (333 - имя дашборда в Jenkins):
```
docker run -d --name jenkins-docker -p 50000:50000 -p 8080:8080 \
-v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home \
-v jenkins-shared-data:/var/jenkins_home/workspace/333/allure-results jenkins-with-docker
```
- параметр -v /var/run/docker.sock:/var/run/docker.sock монтирует доккер соккет хоста в контейнер
- -v jenkins_home:/var/jenkins_home сохраняет данные Jenkins между перезапусками контейнера
- -v jenkins-shared-data:/var/jenkins_home/workspace/333/allure-results создает общий том, к которому потом подключится и поднятый контейнер с тестами

Чтобы у пользователя Jenkins были права на соккет хоста и на запись в общий том,
нужно зайти в контейнер Jenkins с правами администратора:
```
docker exec -it --user root jenkins-docker /bin/sh
```
и выполнить команды:
```
chmod 666 /var/run/dpcker.sock
chown -R jenkins:jenkins /var/jenkins_home/workspace/333/allure-results
chmod -R 755 /var/jenkins_home/workspace/333/allure-results
```

### Внутри контейнера Jenkins (в web интерфейсе Jenkins)
Настраиваем параметры сборки.
Создаем образ с тестами (Dockerfile находится в корне, в Jenkins он скачается с репозитория):
```
docker build -t pytest333 .
```
создаем и запускаем контейнер с тестами с указанием общего тома:
```
docker run -i --rm -v jenkins-shared-data:/app/allure-results pytest333 pytest --remote --url ${url} --executor ${executor} \
--browser ${browser_name} --bv ${browser_version} -n ${number_of_threads} --alluredir=allure-results ./tests
```