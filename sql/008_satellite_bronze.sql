CREATE TABLE IF NOT EXISTS agri.bronze.satellite_scene_metadata(
scene_id STRING,
provider STRING,
acquisition_date DATE,
cloud_cover DOUBLE
) USING DELTA;