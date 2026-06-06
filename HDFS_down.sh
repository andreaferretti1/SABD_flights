#!/bin/bash

docker exec -t master /usr/local/hadoop/sbin/stop-dfs.sh

docker compose -f ./docker/HDFS/docker-compose.yaml down
