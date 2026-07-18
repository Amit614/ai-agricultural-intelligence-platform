CREATE TABLE IF NOT EXISTS agri.bronze.soil_raw(
field_id STRING,
sample_time TIMESTAMP,
ph DOUBLE,
nitrogen DOUBLE,
phosphorus DOUBLE,
potassium DOUBLE,
moisture DOUBLE
) USING DELTA;