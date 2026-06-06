#!/bin/bash

docker exec -t master /usr/local/hadoop/sbin/start-dfs.sh

echo "HDFS launched"