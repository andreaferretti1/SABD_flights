from pyspark.sql import SparkSession

from utils.query1_utils import *

def query1_rdd():

    spark = SparkSession.builder.appName("SABD_query1_rdd").getOrCreate()

    # Carico il dataset
    hdfs_directory = "/progetto_sabd/cleaned_dataset/csv"

    rdd = spark.sparkContext.textFile(hdfs_directory)

    # Formatto i dati
    formatted_rdd = rdd.map(parse_line)

    # Seleziono le compagnie AA e DL
    rdd_to_save = formatted_rdd.filter(lambda element: element[0][0] in {"AA", "DL"})\
            .aggregateByKey(((0, 0), float("-Inf"), float("Inf"), (0, 0)), func_in, func_between)\
            .map(compute_frac) \
            .sortByKey(ascending=True, numPartitions=1) \
            .map(format_data)


    # Salvo i valori in HDFS
    rdd_to_save.saveAsTextFile("/progetto_sabd/results/rdd/query1")



if __name__ == "__main__":
    query1_rdd()
