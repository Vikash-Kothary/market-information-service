#!/bin/bash
# develop.sh - Run local application

docker build -t info_service:0.0.0 .
docker kill info_service
docker run --rm -d --name info_service -p 5000:5000 info_service:0.0.0
