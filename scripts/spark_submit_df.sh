#!/bin/bash

# Preprocessing
docker exec spark-client /opt/spark/bin/spark-submit \
          --master spark://spark-master:7077 \
          --driver-memory 512m \
          --executor-memory 1g \
          --total-executor-cores 4 \
          --executor-cores 2 \
          --conf spark.eventLog.enabled=true\
          /opt/spark/sabd-data/jobs/preprocess/preprocess_df.py

# Query 1
docker exec spark-client /opt/spark/bin/spark-submit \
       --master spark://spark-master:7077 \
       --driver-memory 512m \
       --executor-memory 1g \
       --total-executor-cores 4 \
       --executor-cores 2 \
       --conf spark.eventLog.enabled=true\
        /opt/spark/sabd-data/jobs/query1/query1_df.py

# Query 2
docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        /opt/spark/sabd-data/jobs/query2/query2_df.py
