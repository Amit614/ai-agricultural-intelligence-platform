CREATE TABLE IF NOT EXISTS agri.bronze.weather_raw(
station_id STRING,
event_time TIMESTAMP,
temperature DOUBLE,
humidity DOUBLE,
payload STRING
) USING DELTA;
