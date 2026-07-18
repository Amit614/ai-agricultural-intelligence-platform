CREATE TABLE IF NOT EXISTS agri.gold.sensor_health(
sensor_id STRING,
status STRING,
battery DOUBLE,
event_time TIMESTAMP
) USING DELTA;