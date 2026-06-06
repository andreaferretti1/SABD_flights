#!/bin/bash

docker build -t af/hdfs -f ./docker/HDFS/Dockerfile "$(dirname "$0")"/docker/HDFS

docker compose -f ./docker/HDFS/docker-compose.yaml up -d