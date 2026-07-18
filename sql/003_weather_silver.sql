CREATE TABLE IF NOT EXISTS agri.silver.weather_hourly
USING DELTA AS
SELECT station_id,
date_trunc('hour',event_time) hr,
avg(temperature) avg_temperature,
avg(humidity) avg_humidity
FROM agri.bronze.weather_raw
GROUP BY station_id,date_trunc('hour',event_time);
