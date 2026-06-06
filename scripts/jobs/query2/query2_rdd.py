from pyspark.sql import SparkSession

from utils.query2_utils import *

def query2_rdd():

    spark = SparkSession.builder.appName("SABD_query2_rdd").getOrCreate()


    # Carico il dataset
    hdfs_directory = "/progetto_sabd/cleaned_dataset/csv"
    rdd = spark.sparkContext.textFile(hdfs_directory)


    # Formatto i dati

    formatted_rdd = rdd.rdd = rdd.map(parse_line)


                                            # canc_div, arr_delay_mean, cause_del
    rdd_to_save = formatted_rdd.aggregateByKey((0, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)), func_in, func_between)\
                .map(compute_avgs)\
                .filter(lambda record: record[1][0] >= 500)\
                .sortBy(lambda record: record[1][1], ascending = False)\
                .zipWithIndex()\
                .filter(lambda pair: pair[1] < 10)\
                .map(lambda pair: format_data(pair[0]))\
                .coalesce(1)


    #Salvo il risultto su HDFS
    rdd_to_save.saveAsTextFile("/progetto_sabd/results/rdd/query2")






if __name__ == "__main__":
    query2_rdd()
