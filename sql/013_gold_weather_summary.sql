CREATE OR REPLACE VIEW agri.gold.weather_summary AS
SELECT hour,event_time_count,avg_temperature FROM (
SELECT HOUR(event_time) hour,COUNT(*) event_time_count,AVG(temperature) avg_temperature
FROM agri.silver.weather_hourly
GROUP BY HOUR(event_time));