#! /bin/bash


cd "$(dirname "$0")"/../scripts || exit

echo "Zipping dependencies"

zip -r dependencies.zip utils || exit

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

# Query 1
docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        --py-files /opt/spark/sabd-data/dependencies.zip \
        /opt/spark/sabd-data/jobs/query1/query1_rdd.py

# Query 2
docker exec spark-client /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --driver-memory 512m \
        --executor-memory 1g \
        --total-executor-cores 4 \
        --executor-cores 2 \
        --conf spark.eventLog.enabled=true\
        --py-files /opt/spark/sabd-data/dependencies.zip \
        /opt/spark/sabd-data/jobs/query2/query2_rdd.py


# Rimuovo dipendenze
rm dependencies.zip