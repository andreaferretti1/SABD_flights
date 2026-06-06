from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def preprocessing():

    spark = SparkSession.builder.appName("SABD_preprocess_df").getOrCreate()

    # Specifico directory input e output
    hdfs_in_dir = "/progetto_sabd/dataset"
    hdfs_parquet_out_dir = "/progetto_sabd/cleaned_dataset/parquet"

    df = spark.read.csv(hdfs_in_dir,
                        header = True,
                        inferSchema = False)


    # Seleziono le colonne necessarie per le query e gli assegno il tipo
    processed_df = df.select(
        F.col("MONTH"),
        F.col("OP_UNIQUE_CARRIER"),
        F.col("DEP_DELAY").cast("float"),
        F.col("ARR_DELAY").cast("float"),
        F.col("CANCELLED").cast("float"),
        F.col("DIVERTED").cast("float"),
        F.col("CARRIER_DELAY").cast("float"),
        F.col("WEATHER_DELAY").cast("float"),
        F.col("NAS_DELAY").cast("float"),
        F.col("SECURITY_DELAY").cast("float"),
        F.col("LATE_AIRCRAFT_DELAY").cast("float")
    )


    # Salvo i file su HDFS in formato parquet per query con DataFrame
    processed_df.write \
    .mode("overwrite") \
    .partitionBy("MONTH") \
    .option("compression", "lz4") \
    .parquet(hdfs_parquet_out_dir)



if __name__ == "__main__":
    preprocessing()