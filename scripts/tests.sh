#!/bin/bash
# tests.sh - Run tests

docker build -t info_service:0.0.0 .
docker kill info_service
docker run --rm -d --name info_service -p 5000:5000 info_service:0.0.0
docker exec -it info_service python -m unittest
