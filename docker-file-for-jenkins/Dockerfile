FROM jenkins/jenkins:lts

# Установите необходимые пакеты
USER root
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Вернуться к пользователю Jenkins
USER jenkins



docker run -d --name jenkins-docker -p 50000:50000 -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins-with-docker