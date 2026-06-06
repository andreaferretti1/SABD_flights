#! /bin/bash


cd "$(dirname "$0")"/../../../scripts || exit

echo "Zipping dependencies"

zip -r dependencies.zip utils || exit


# Preprocessing
  docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --name "preprocess_rdd_1work_2core"\
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        --py-files /opt/spark/sabd-data/dependencies.zip \
        /opt/spark/sabd-data/jobs/preprocess/preprocess_rdd.py

for execution in $(seq 1 10);
do

  # Query 2
  docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --name "query2_rdd_1work_2core"\
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        --py-files /opt/spark/sabd-data/dependencies.zip \
        /opt/spark/sabd-data/jobs/query2/query2_rdd.py


  # Rimuovo risultati query da HDFS
  docker exec master hdfs dfs -rm -r /progetto_sabd/results/rdd

done

# Rimuovo file parquet da HDFS
docker exec master hdfs dfs -rm -r /progetto_sabd/cleaned_dataset/csv

# Rimuovo dipendenza
rm dependencies.zip