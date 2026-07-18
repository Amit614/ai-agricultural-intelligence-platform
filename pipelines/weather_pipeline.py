from pyspark import pipelines as dp
from pyspark.sql.functions import col,hour,avg

@dp.table(name="weather_bronze")
def weather_bronze():
    return spark.read.table("agri.bronze.weather_raw")

@dp.expect_or_drop("valid_temp","temperature BETWEEN -80 AND 70")
@dp.table(name="weather_silver")
def weather_silver():
    return weather_bronze().select("station_id","event_time","temperature","humidity")

@dp.table(name="weather_gold")
def weather_gold():
    return weather_silver().groupBy(hour(col("event_time")).alias("hour")).agg(avg("temperature").alias("avg_temperature"))
