CREATE OR REPLACE VIEW agri.gold.v_field_summary AS
SELECT f.field_id,
       w.avg_temperature,
       f.avg_moisture
FROM agri.gold.field_fertility f
LEFT JOIN agri.silver.weather_hourly w
ON 1=1;
