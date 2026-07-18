from pyspark import pipelines as dp
@dp.table(name="soil_silver")
def soil_silver():
    return spark.read.table("agri.bronze.soil_raw")
