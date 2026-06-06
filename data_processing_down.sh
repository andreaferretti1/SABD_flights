#!/bin/bash

# Fermo esecuzione Spark
./Spark_down.sh

# Fermo esecuzione HDFS
./HDFS_down.sh

docker network rm sabd_net