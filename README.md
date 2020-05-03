# docker_compose_webserver
It is a TUI program to launch multiple webserver simultaneously  in linux platform. This project is based on docker-compose to lauch your desired webserver within less amount of time.
# Project Title
## Docker Installation in Linux platform (redhat/centos)
Yum configuration for adding docker repo<br>
using "https://download.docker.com/linux/centos/docker-ce.repo" put this link in the file in /etc/yum.repos.d/

![alt text](https://github.com/aakash1003/docker_compose_webserver/blob/master/docker_repo.PNG) 

Now run that command

``` html
yum install docker --nobest
```

## Start Docker
``` html
systemctl start docker
```

## Installing Docker Compose
``` html
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
