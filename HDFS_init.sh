#!/bin/bash


# Formattazione
docker exec -t master hdfs namenode -format

# Avvio datanode
./HDFS_start.sh

# Creazione directory in cui salvare il dataset
docker exec -t master hdfs dfs -mkdir -p /progetto_sabd/dataset

# Assegno possesso cartella a nifi e cmabio permessei per permettere a NiFi di scrivere
docker exec -t master hdfs dfs -chown nifi:nifi /progetto_sabd/dataset
docker exec -t master hdfs dfs -chmod 755 /progetto_sabd/dataset


echo "HDFS initialized"