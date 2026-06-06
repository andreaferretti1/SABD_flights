from pyspark.sql import SparkSession

from pyspark.sql import functions as F

def query1_df():

    spark = SparkSession.builder.appName("SABD_query1_df").getOrCreate()

    # Carico il dataset
    hdfs_directory = "/progetto_sabd/cleaned_dataset/parquet"
    df = spark.read.parquet(hdfs_directory)

    # Seleziono le colonne necessarie per la query e converto in rdd
    cols_to_process = ["MONTH", "OP_UNIQUE_CARRIER", "DEP_DELAY", "CANCELLED"]
    final_cols = ["month", "airline", "dep-delay-mean", "dep-delay-min", "dep-delay-max", "cancellation-rate"]

    # Calcolo le statistiche
    result_df = df.select(*cols_to_process)\
                    .filter("OP_UNIQUE_CARRIER='AA' OR OP_UNIQUE_CARRIER='DL'") \
                    .groupBy("MONTH", "OP_UNIQUE_CARRIER") \
                    .agg(
                        F.round(F.avg(F.when(F.col("CANCELLED") == 0, F.col("DEP_DELAY"))), 2).alias("dep-delay-mean"),
                        F.round(F.min(F.when(F.col("CANCELLED") == 0, F.col("DEP_DELAY"))), 2).alias("dep-delay-min"),
                        F.round(F.max(F.when(F.col("CANCELLED") == 0, F.col("DEP_DELAY"))), 2).alias("dep-delay-max"),
                        F.round((F.sum("CANCELLED") / F.count("CANCELLED")), 2).alias("cancellation-rate")
                    )\
                    .withColumnRenamed("MONTH", "month") \
                    .withColumnRenamed("OP_UNIQUE_CARRIER", "airline") \
                    .select(*final_cols)\
                    .coalesce(1)\
                    .sort("airline", "month", ascending = True)



    # Salvo i dati
    result_df.write\
               .format("csv")\
               .option("header", "true")\
               .save("/progetto_sabd/results/dataframe/query1")




if __name__ == "__main__":
    query1_df()