CREATE OR REFRESH STREAMING TABLE agri.silver.sensor_events
AS SELECT * FROM STREAM agri.bronze.sensor_events;
