from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
df=spark.table('agri.bronze.weather_raw')
(df.groupByExpr("station_id","date_trunc('hour',event_time) as hr")
 .avg("temperature","humidity")
 .write.mode("overwrite")
 .saveAsTable("agri.silver.weather_hourly"))
