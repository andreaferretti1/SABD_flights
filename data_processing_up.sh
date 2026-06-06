#!/bin/bash

docker network create sabd_net

# Avvio HDFS
./HDFS_up.sh
./HDFS_start.sh

#Avvio Spark
./Spark_up.sh
