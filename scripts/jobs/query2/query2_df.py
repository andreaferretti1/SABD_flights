from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def query2_df():

    spark = SparkSession.builder.appName("SABD_query2_df").getOrCreate()

    cols_to_process = ["OP_UNIQUE_CARRIER", "CANCELLED", "DIVERTED", "ARR_DELAY", "CARRIER_DELAY", "WEATHER_DELAY",
                       "NAS_DELAY", "SECURITY_DELAY", "LATE_AIRCRAFT_DELAY"]
    # Carico il dataset
    hdfs_directory = "/progetto_sabd/cleaned_dataset/parquet"

    df = spark.read.parquet(hdfs_directory)\
            .select(*cols_to_process)\


    result_df = df.groupBy("OP_UNIQUE_CARRIER")\
                .agg(F.count(F.when((F.col("CANCELLED") == 0) & (F.col("DIVERTED") == 0), 1)).alias("num_flights"),
                     F.round(F.avg( "ARR_DELAY"), 2).alias("arr_delay_mean"),
                     F.round(F.avg("CARRIER_DELAY"), 2).alias("carrier_delay_mean"),
                     F.round(F.avg("WEATHER_DELAY"), 2).alias("weather_delay_mean"),
                     F.round(F.avg("NAS_DELAY"), 2).alias("nas_delay_mean"),
                     F.round(F.avg("SECURITY_DELAY"), 2).alias("security_delay_mean"),
                     F.round(F.avg("LATE_AIRCRAFT_DELAY"), 2).alias("late_aircraft_delay_mean"))\
                .withColumnRenamed("OP_UNIQUE_CARRIER", "carrier")



    top10_df = result_df.filter(F.col("num_flights") >= 500) \
                .coalesce(1) \
                .sort("arr_delay_mean", ascending = False)\
                .limit(10)


    top10_df.write \
        .format("csv") \
        .option("header", "true") \
        .save("/progetto_sabd/results/dataframe/query2")




if __name__ == "__main__":
    query2_df()