CREATE OR REFRESH STREAMING TABLE agri.quarantine.invalid_records AS
SELECT * FROM STREAM agri.bronze.sensor_events WHERE sensor_id IS NULL;
