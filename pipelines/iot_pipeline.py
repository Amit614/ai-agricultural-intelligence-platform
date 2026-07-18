from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
df=(spark.readStream.format('delta')
    .table('agri.bronze.sensor_raw'))
(df.writeStream
 .option('checkpointLocation','dbfs:/checkpoints/iot')
 .toTable('agri.silver.sensor_readings'))
