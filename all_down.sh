#!/bin/bash

# Distruggo container HDFS
./HDFS_down.sh

# Distruggo container Redis
./Redis_down.sh

# Distruggo container NiFi
./NiFi_down.sh

# Distruggo container Spark
./Spark_down.sh

# Distruggo container Graphana
./Graphana_down.sh

# Elimino la rete
docker network rm sabd_net

echo "Container rimossi"