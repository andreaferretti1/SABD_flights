#!/bin/bash

cd "$(dirname "$0")"/../../../scripts || exit

echo "Zipping dependencies"

zip -r dependencies.zip utils || exit

for execution in $(seq 1 10);
do
# Preprocessing
  docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        --py-files /opt/spark/sabd-data/dependencies.zip \
        /opt/spark/sabd-data/jobs/preprocess/preprocess_rdd.py
  
  
  # Rimuovo file csv da HDFS
  docker exec master hdfs dfs -rm -r /progetto_sabd/cleaned_dataset/csv
        
done

# Rimuovo dipendenze
rm dependencies.zip