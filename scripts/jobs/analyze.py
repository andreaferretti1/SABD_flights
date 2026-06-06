from pyspark.sql import functions as F
from pyspark.sql import SparkSession

def analyze_data():

    spark = SparkSession.builder.appName("SABD_analyze").getOrCreate()

    # Specifico directory input
    hdfs_in_dir = "/progetto_sabd/dataset"

    # Specifico file da preprocessare
    files_to_preprocess = ["202504_T_ONTIME_REPORTING", "202503_T_ONTIME_REPORTING", "202502_T_ONTIME_REPORTING", "202501_T_ONTIME_REPORTING"]
    pathfiles = [f"{hdfs_in_dir}/{file}.csv.snappy" for file in files_to_preprocess]

    df = spark.read.csv(pathfiles,
                        header = True,
                        inferSchema = False)

    df.groupBy("MONTH").count().show(vertical = True)

    df.groupby("MONTH").agg(*[F.count(F.when(F.isnull(c), c)).alias(c) for c in df.columns]).show(vertical = True)

    no_cancelled = F.col("CANCELLED") == "0.00"
    delay = (F.col("ARR_DELAY") != "0.00") | (F.col("DEP_DELAY") != "0.00")

    df.groupby("MONTH").agg(F.count(F.when((F.isnull("DEP_DELAY")) & no_cancelled, 1)).alias("dep_delay_null_and_not_canc"),
                            F.count(F.when((F.isnull("ARR_DELAY")) & no_cancelled, 1)).alias("arr_delay_null_and_not_canc"),
                            F.count(F.when((F.isnull("CARRIER_DELAY")) & delay, 1)).alias("carrier_delay_null_and_delay"),
                            F.count(F.when((F.isnull("NAS_DELAY")) & delay, 1)).alias("nas_delay_and_delay"),
                            F.count(F.when((F.isnull("SECURITY_DELAY")) & delay, 1)).alias("security_delay_and_delay"),
                            F.count(F.when((F.isnull("WEATHER_DELAY")) & delay, 1)).alias("weather_delay_and_delay"),
                            F.count(F.when((F.isnull("LATE_AIRCRAFT_DELAY")) & delay, 1)).alias("late_aircraft_delay_and_delay"))\
        .show(vertical = True)


    df.groupby("OP_UNIQUE_CARRIER").agg(
        F.round((F.count(F.when((F.isnull("DEP_DELAY")) & no_cancelled, 1))) / F.count("*") * 100, 2).alias("dep_delay_null_and_not_canc_percentage"),
        F.round(F.count(F.when((F.isnull("ARR_DELAY")) & no_cancelled, 1)) / F.count("*") * 100, 2).alias("arr_delay_null_and_not_canc_percentage"),
        F.round(F.count(F.when((F.isnull("CARRIER_DELAY")) & delay, 1)) / F.count("*") * 100, 2).alias("carrier_delay_null_and_delay_percentage"),
        F.round(F.count(F.when((F.isnull("NAS_DELAY")) & delay, 1)) / F.count("*") * 100, 2).alias("nas_delay_and_no_delay_percentage"),
        F.round(F.count(F.when((F.isnull("SECURITY_DELAY")) & delay, 1)) / F.count("*") * 100, 2).alias("security_delay_and_no_delay_percentage"),
        F.round(F.count(F.when((F.isnull("WEATHER_DELAY")) & delay, 1)) / F.count("*") * 100, 2).alias("weather_delay_and_no_delay_percentage"),
        F.round(F.count(F.when((F.isnull("LATE_AIRCRAFT_DELAY")) & delay, 1)) / F.count("*") * 100, 2).alias("late_aircraft_delay_and_no_delay_percentage")) \
        .show(vertical=True)






if __name__ == "__main__":
    anlyze_data()