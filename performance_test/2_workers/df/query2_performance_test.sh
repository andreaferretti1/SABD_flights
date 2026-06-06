#! /bin/bash


# Preprocessing
  docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        /opt/spark/sabd-data/jobs/preprocess/preprocess_df.py

for execution in $(seq 1 10);
do
  # Query 2
  docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        /opt/spark/sabd-data/jobs/query2/query2_df.py




  # Rimuovo risultati query da HDFS
  docker exec master hdfs dfs -rm -r /progetto_sabd/results/dataframe

done

# Rimuovo file parquet da HDFS
docker exec master hdfs dfs -rm -r /progetto_sabd/cleaned_dataset/parquet
