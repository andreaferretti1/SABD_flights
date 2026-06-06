#!/bin/bash

docker build -t af/nifi -f ./docker/NiFi/Dockerfile "$(dirname "$0")"/docker

docker compose -f ./docker/NiFi/docker-compose.yaml up -d