#!/bin/bash

# Creo rete
docker network create sabd_net

# Istanzio container HDFS
./HDFS_up.sh
./HDFS_start.sh

# Istanzio container Redis
./Redis_up.sh

# Istanzio container NiFi
./NiFi_up.sh

echo "Container creati"