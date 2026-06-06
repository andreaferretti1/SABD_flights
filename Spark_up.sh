#!/bin/bash

docker build -t af/spark -f ./docker/Spark/Dockerfile "$(dirname "$0")"/docker

docker compose -f ./docker/Spark/docker-compose.yaml up -d