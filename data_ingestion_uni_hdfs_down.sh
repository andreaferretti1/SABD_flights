#!/bin/bash

# Distruggo il container NiFi
./NiFi_down.sh

# Distruggo i container HDFS
./HDFS_down.sh

# Elimino la rete
docker network rm sabd_net