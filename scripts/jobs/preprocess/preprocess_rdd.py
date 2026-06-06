from pyspark.sql import SparkSession

from utils.preprocess_rdd_utils import parse_and_map_line

def preprocess():
    spark = SparkSession.builder.appName("SABD_preprocess_rdd").getOrCreate()

    hdfs_dir_in  = "/progetto_sabd/dataset"
    hdfs_dir_out = "/progetto_sabd/cleaned_dataset/csv"

    rdd = spark.sparkContext.textFile(hdfs_dir_in)

    # Rimuovo header
    header = rdd.first()
    no_header_rdd = rdd.filter(lambda line: line != header)

    # Faccio parsing e converto in record da salvare
    no_header_rdd.map(parse_and_map_line).saveAsTextFile(hdfs_dir_out)


if __name__ == "__main__":
    preprocess()