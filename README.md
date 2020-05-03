# docker_compose_webserver
It is a TUI program to launch multiple webserver simultaneously  in linux platform. This project is based on docker-compose to lauch your desired webserver within less amount of time.
# Project Title
It is a TUI program in which a python file is used to launch the webservers, where you can launch any webserver you want according to your will. All the webservers all using different port numbers
thus user can launch multiple webservers simultaneously.
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

# Cloning the project
``` html
git clone https://github.com/aakash1003/docker_compose_webserver.git
```
## TO Run Python File:
``` html
python3 menu.py
```
![alt text](https://github.com/aakash1003/docker_compose_webserver/blob/master/menu.PNG)
![alt text](https://github.com/aakash1003/docker_compose_webserver/blob/master/web1.PNG)(https://github.com/aakash1003/docker_compose_webserver/blob/master/web4.PNG)

## port No. used:
`8081` : To launch Wordpress 

`8082` : To launch Nginx

`8083` : To launch ghost

`8084` : To launch drupal

`8085` : To launch owncloud
