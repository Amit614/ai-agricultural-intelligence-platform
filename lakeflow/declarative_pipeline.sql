CREATE OR REFRESH STREAMING TABLE agri_gold.crop_events AS
SELECT * FROM STREAM agri_silver.crop_events;