CREATE TABLE IF NOT EXISTS agri.bronze.sensor_raw(
sensor_id STRING,
field_id STRING,
event_time TIMESTAMP,
temperature DOUBLE,
moisture DOUBLE,
battery DOUBLE
) USING DELTA;