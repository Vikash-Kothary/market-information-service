#!/bin/bash
# clear_docker.sh

docker rmi $(docker images -a -q) -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q) -f
docker volume rm $(docker volume ls -q) -f