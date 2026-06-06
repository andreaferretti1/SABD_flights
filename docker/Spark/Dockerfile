FROM apache/spark:4.1.2-scala2.13-java17-python3-r-ubuntu

USER root

WORKDIR /opt/spark

# Configuro HDFS
COPY HDFS/core-site.xml /etc/hadoop/core-site.xml

COPY HDFS/hdfs-site.xml /etc/hadoop/hdfs-site.xml

RUN mkdir -p /opt/spark/conf && echo "export HADOOP_CONF_DIR=/etc/hadoop" >> /opt/spark/conf/spark-env.sh

USER spark