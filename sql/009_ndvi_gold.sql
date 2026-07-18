CREATE TABLE IF NOT EXISTS agri.gold.field_ndvi(
field_id STRING,
scene_id STRING,
ndvi DOUBLE,
acquisition_date DATE
) USING DELTA;